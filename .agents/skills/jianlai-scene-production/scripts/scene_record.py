#!/usr/bin/env python3
"""Scene production records: structural gates, provenance and bounded retries.

No image generation or visual judgement. Only init writes a file.
"""
import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

STAGES = {
    "brief": ("source_scope", "narrative_focus"),
    "references": ("identity_basis", "reference_roles"),
    "composition": ("story_relation", "framing", "staging"),
    "space": ("layout", "grounding", "staging"),
    "sketch": ("identity", "anatomy", "continuity", "staging"),
    "color": ("identity", "structure_preserved", "palette_light", "staging"),
    "preview": ("identity", "actual_composite", "dialogue_safe_area", "staging"),
    "delivery": ("identity", "provenance", "adoption_scope", "staging"),
}
IDENTITY_STAGES = {"sketch", "color", "preview", "delivery"}
STAGING_STAGES = {"composition", "space"} | IDENTITY_STAGES
STAGING_FIELDS = ("position", "footing", "facing", "gaze", "scale_depth", "occlusion")
SCENE_STAGING_FIELDS = ("camera", "action_target", "action_space", "route", "continuity")
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff"}
CONDITIONAL = {"identity_basis", "identity", "anatomy", "grounding",
               "actual_composite", "dialogue_safe_area", "staging"}
BOUNDARY = "Only record structure and file fingerprints are checked; visual quality and user approval are not established by this tool."


def staging_digest(plan):
    return hashlib.sha256(json.dumps(plan, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint(path, role="reference"):
    path = Path(path).resolve(strict=True)
    if not path.is_file():
        raise ValueError("Fingerprint target must be a file")
    return {"path": str(path), "sha256": digest(path), "role": role}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate(record, record_path):
    errors, blockers = [], []
    base = Path(record_path).resolve().parent
    seen_outputs = {}

    def need(condition, message):
        if not condition:
            errors.append(message)
        return condition

    def obj(value, label):
        return value if need(isinstance(value, dict), label + " must be an object") else {}

    def items(value, label):
        return value if need(isinstance(value, list), label + " must be a list") else []

    def signatures(entries):
        if not isinstance(entries, list):
            return set()
        return {(str((base / x["path"]).resolve()).casefold() if sys.platform == "win32" else str((base / x["path"]).resolve()), x["sha256"].lower())
                for x in entries if isinstance(x, dict) and nonempty(x.get("path")) and nonempty(x.get("sha256"))}

    def files(value, label, required=False, output_owner=None):
        entries = items(value, label)
        need(not required or bool(entries), label + " needs at least one fingerprint")
        for index, entry in enumerate(entries):
            loc = f"{label}[{index}]"
            entry = obj(entry, loc)
            path = entry.get("path")
            checksum = entry.get("sha256")
            need(nonempty(entry.get("role")), loc + ".role is required")
            path_ok = need(nonempty(path), loc + ".path is required")
            hash_ok = need(isinstance(checksum, str) and bool(re.fullmatch(r"[0-9a-fA-F]{64}", checksum)), loc + ".sha256 must be a SHA256 digest")
            if path_ok and hash_ok:
                target = (base / path).resolve()
                try:
                    need(target.is_file(), loc + " file is missing: " + str(target))
                    if target.is_file():
                        need(digest(target) == checksum.lower(), loc + " fingerprint changed: " + str(target))
                except OSError as exc:
                    errors.append(loc + " cannot read file: " + str(exc))
                if output_owner:
                    key = str(target).casefold() if sys.platform == "win32" else str(target)
                    prior = seen_outputs.get(key)
                    reusable = prior and prior[0].split("-")[0] != output_owner.split("-")[0] and prior[1] == checksum.lower()
                    need(prior is None or prior[0] == output_owner or reusable,
                         loc + " reuses a previous attempt output path; preserve immutable outputs")
                    seen_outputs[key] = (output_owner, checksum.lower())
        return entries

    record = obj(record, "record")
    need(record.get("schema_version") == 2,
         "schema_version must be 2; v1 is historical only: recover actual identity inputs and reviews before continuing, never relabel old passes")
    task = obj(record.get("task"), "task")
    for field in ("scene_id", "request", "project_root", "authorization"):
        need(nonempty(task.get(field)), "task." + field + " is required")
    need(task.get("scope") in ("candidate", "integrate"), "task.scope must be candidate or integrate")
    stop_after = task.get("stop_after_stage", "delivery")
    valid_stop = need(isinstance(stop_after, str) and stop_after in STAGES, "task.stop_after_stage must name a production stage")
    stop_index = list(STAGES).index(stop_after) if valid_stop else len(STAGES) - 1
    need(task.get("scope") != "integrate" or stop_after == "delivery", "integrate scope requires stop_after_stage=delivery")
    size = task.get("target_size")
    need(isinstance(size, list) and len(size) == 2 and all(type(x) is int and x > 0 for x in size), "task.target_size needs two positive integers")
    if nonempty(task.get("project_root")):
        need(Path(task["project_root"]).is_absolute() and Path(task["project_root"]).is_dir(), "task.project_root must be an existing absolute directory")
    sources = files(record.get("sources"), "sources")
    identity = obj(record.get("identity"), "identity")
    characters = {}
    for ci, raw_character in enumerate(items(identity.get("characters"), "identity.characters")):
        label = f"identity.characters[{ci}]"
        character = obj(raw_character, label)
        cid = character.get("id")
        if need(nonempty(cid), label + ".id is required"):
            need(cid not in characters, label + ": duplicate character id")
            characters[cid] = character
        need(character.get("visibility") in ("visible", "not_visible"), label + ": invalid visibility")
        if character.get("visibility") == "not_visible":
            need(nonempty(character.get("visibility_reason")), label + ": not_visible needs a narrative occlusion/back-view reason, not low resolution")
        for field in ("face_master", "standard"):
            entry = files([character.get(field)], label + "." + field, required=True)
            need(signatures(entry) <= signatures(sources), label + "." + field + " must be bound to sources")
        master = character.get("face_master")
        if isinstance(master, dict) and nonempty(master.get("path")):
            need(Path(master["path"]).suffix.lower() in IMAGE_SUFFIXES, label + ".face_master must be an image")
    absence = identity.get("absence_reason")
    need(isinstance(absence, str), "identity.absence_reason must be a string")
    if characters:
        need(not absence, "identity.absence_reason must be empty when characters are present")
    face_masters = [c.get("face_master") for c in characters.values()]

    staging = obj(record.get("staging", {}), "staging")
    raw_stages = record.get("stages")
    staging_started = isinstance(raw_stages, dict) and any(
        isinstance(raw_stages.get(name), dict) and
        (raw_stages[name].get("attempts") or raw_stages[name].get("status") == "passed")
        for name in STAGING_STAGES)
    staging_required = bool(characters) and staging_started
    if staging_required:
        for field in ("anchors",) + SCENE_STAGING_FIELDS:
            need(nonempty(staging.get(field)), "staging." + field + " needs a concrete scene plan")
    staging_evidence = files(staging.get("evidence", []), "staging.evidence", required=staging_required)
    need(signatures(staging_evidence) <= signatures(sources), "staging.evidence must be bound to sources")
    staging_characters = []
    for ci, raw_placement in enumerate(items(staging.get("characters", []), "staging.characters")):
        label = f"staging.characters[{ci}]"
        placement = obj(raw_placement, label)
        cid = placement.get("character_id")
        need(isinstance(cid, str) and cid in characters, label + ": unknown character_id")
        need(cid not in staging_characters, label + ": duplicate character placement")
        staging_characters.append(cid)
        if staging_required:
            for field in STAGING_FIELDS:
                need(nonempty(placement.get(field)), label + "." + field + " needs a concrete staging target")
    if staging_required:
        need(len(staging_characters) == len(characters) and all(cid in staging_characters for cid in characters),
             "staging.characters must cover every character exactly once")
    staging_sha256 = staging_digest(staging) if characters else None

    def identity_input(attempt, inputs, label):
        if not characters or attempt.get("kind") != "image":
            return
        need(signatures(face_masters) <= signatures(inputs), label + ": every face master must be in this attempt's inputs")
        binding = obj(attempt.get("identity_input"), label + ".identity_input")
        completed = bool(attempt.get("outputs")) or attempt.get("review") is not None
        method = binding.get("method")
        need(method in ("reference_images", "preserved_pixels"), label + ": invalid identity_input.method")
        if method == "reference_images":
            if completed:
                need(nonempty(binding.get("call_id")), label + ": actual image tool call_id is required")
            args = obj(binding.get("arguments"), label + ".identity_input.arguments")
            need(args.get("prompt") == attempt.get("prompt"), label + ": recorded tool prompt must match the attempt prompt")
            paths = items(args.get("referenced_image_paths"), label + ".identity_input.arguments.referenced_image_paths")
            need(all(nonempty(x) and Path(x).is_absolute() for x in paths), label + ": actual image references must be absolute paths")
            def key(path):
                value = str((base / path).resolve())
                return value.casefold() if sys.platform == "win32" else value
            actual = {key(path) for path in paths if nonempty(path)}
            need(all(key(m["path"]) in actual for m in face_masters if isinstance(m, dict) and nonempty(m.get("path"))),
                 label + ": actual tool request is missing a face master")
            need(not args.get("num_last_images_to_include"), label + ": use explicit local face reference paths, not an unbound recent-image count")
        elif method == "preserved_pixels":
            source = files([binding.get("source")], label + ".identity_input.source", required=True)
            need(signatures(source) <= signatures(inputs), label + ": preserved pixel source must be in inputs")
            files(binding.get("evidence", []), label + ".identity_input.evidence", required=completed)

    def character_review(attempt, review, inputs, outputs, label, identity_result, staging_result):
        entries = items(review.get("character_checks", []), label + ".review.character_checks")
        found = []
        reviewed_images = set()
        passable = True
        placement_passable = True
        for ci, raw_check in enumerate(entries):
            loc = f"{label}.review.character_checks[{ci}]"
            check = obj(raw_check, loc)
            cid = check.get("character_id")
            known = isinstance(cid, str) and cid in characters
            need(known, loc + ": unknown character_id")
            need(cid not in found, loc + ": duplicate character review")
            found.append(cid)
            result = check.get("result")
            need(result in ("pass", "fail", "unverified", "not_applicable"), loc + ": invalid identity result")
            for field in ("observation", "view"):
                need(nonempty(check.get(field)), loc + "." + field + " is required")
            picture = files([check.get("image")], loc + ".image", required=True)
            if isinstance(check.get("image"), dict) and nonempty(check["image"].get("path")):
                need(Path(check["image"]["path"]).suffix.lower() in IMAGE_SUFFIXES, loc + ": reviewed image must be an image file")
            image_outputs = [entry for entry in outputs if isinstance(entry, dict) and nonempty(entry.get("path")) and Path(entry["path"]).suffix.lower() in IMAGE_SUFFIXES]
            current = outputs if attempt.get("kind") == "image" else image_outputs or inputs
            need(signatures(picture) <= signatures(current), loc + ": reviewed image must belong to this attempt's current image outputs (or unchanged input when no image is output)")
            reviewed_images.update(signatures(picture))
            if not image_outputs and last_passed_identity_image:
                need(signatures(picture) == last_passed_identity_image, loc + ": unchanged-image review must follow the last passed identity-reviewed image")
            evidence = files(check.get("evidence"), loc + ".evidence", required=True)
            need(signatures(picture) <= signatures(evidence), loc + ": identity evidence must include the reviewed image")
            if known:
                character = characters[cid]
                need(signatures([character.get("face_master")]) <= signatures(evidence), loc + ": identity evidence must include this character's face master")
                if result == "not_applicable":
                    need(character.get("visibility") == "not_visible", loc + ": a visible face cannot waive identity review")
                if result == "pass":
                    need(character.get("visibility") == "visible", loc + ": hidden faces cannot claim a facial identity pass")
            if result == "pass":
                comparisons = obj(check.get("comparisons"), loc + ".comparisons")
                for field in ("face_shape", "features", "age", "hair"):
                    need(nonempty(comparisons.get(field)), loc + ".comparisons." + field + " needs a concrete comparison")
            if result not in ("pass", "not_applicable"):
                passable = False
            placement = obj(check.get("placement"), loc + ".placement")
            placement_result = placement.get("result")
            need(placement_result in ("pass", "fail", "unverified"), loc + ".placement: invalid result")
            need(nonempty(placement.get("observation")), loc + ".placement.observation is required")
            if placement_result == "pass":
                observations = obj(placement.get("observations"), loc + ".placement.observations")
                for field in STAGING_FIELDS:
                    need(nonempty(observations.get(field)), loc + ".placement.observations." + field + " needs a concrete comparison")
            else:
                placement_passable = False
        need(len(found) == len(characters) and all(cid in found for cid in characters), label + ": identity review must cover every character exactly once")
        need(len(reviewed_images) <= 1, label + ": every character must be reviewed in the same single scene image")
        if any(c.get("visibility") == "visible" for c in characters.values()):
            need(identity_result != "not_applicable", label + ": visible characters require an identity check")
        if not passable:
            need(identity_result not in ("pass", "not_applicable") and review.get("verdict") != "pass", label + ": failed/unverified character identity cannot pass")
        if not placement_passable:
            need(staging_result not in ("pass", "not_applicable") and review.get("verdict") != "pass",
                 label + ": failed/unverified character placement cannot pass staging or the review")
        return reviewed_images

    history_counts = {stage: 0 for stage in STAGES}
    history_extensions = {stage: 0 for stage in STAGES}
    extension_keys = set()
    cursor, cursor_base = record, base
    visited = {str(Path(record_path).resolve()).casefold()}
    while "previous_record" in cursor:
        need(nonempty(cursor.get("revision_reason")), "continuation record requires revision_reason")
        link = obj(cursor["previous_record"], "previous_record")
        if not need(nonempty(link.get("path")) and nonempty(link.get("sha256")) and nonempty(link.get("role")), "previous_record needs path, sha256 and role"):
            break
        target = (cursor_base / link["path"]).resolve()
        key = str(target).casefold()
        if not need(key not in visited and len(visited) < 64, "previous_record chain is cyclic or exceeds 63 revisions"):
            break
        visited.add(key)
        try:
            if not need(target.is_file() and digest(target) == link["sha256"].lower(), "previous_record fingerprint changed or file missing: " + str(target)):
                break
            cursor = obj(json.loads(target.read_text(encoding="utf-8-sig")), "previous record")
        except (OSError, ValueError) as exc:
            errors.append("Cannot load previous record: " + str(exc))
            break
        need(cursor.get("schema_version") in (1, 2), "previous record must use schema_version 1 or 2")
        prior_task = obj(cursor.get("task"), "previous task")
        need(prior_task.get("scene_id") == task.get("scene_id"), "previous record must belong to the same scene_id")
        prior_stages = obj(cursor.get("stages"), "previous stages")
        for stage_name in STAGES:
            prior_stage = obj(prior_stages.get(stage_name), "previous " + stage_name)
            history_counts[stage_name] += len(items(prior_stage.get("attempts"), "previous attempts"))
        prior_retry = obj(cursor.get("retry_policy"), "previous retry_policy")
        for extension in items(prior_retry.get("extensions"), "previous extensions"):
            extension = obj(extension, "previous extension")
            stage_name, count = extension.get("stage"), extension.get("extra_reworks")
            if need(isinstance(stage_name, str) and stage_name in STAGES and type(count) is int and count > 0 and nonempty(extension.get("authorization")), "invalid previous retry extension"):
                extension_key = (stage_name, count, extension["authorization"])
                if need(extension_key not in extension_keys, "retry authorization is duplicated across previous records"):
                    history_extensions[stage_name] += count
                    extension_keys.add(extension_key)
        cursor_base = target.parent
    constraints = obj(record.get("constraints"), "constraints")
    for field in ("locked", "allowed_changes", "uncertainties"):
        values = items(constraints.get(field), "constraints." + field)
        need(all(nonempty(x) for x in values), "constraints." + field + " entries must be nonempty strings")
    if constraints.get("uncertainties"):
        blockers.append("Unresolved constraints.uncertainties require a decision before production continues")

    retry = obj(record.get("retry_policy"), "retry_policy")
    need(retry.get("max_reworks") == 2, "retry_policy.max_reworks is fixed at 2; use authorized extensions")
    limits = {stage: 3 + history_extensions[stage] for stage in STAGES}
    for index, extension in enumerate(items(retry.get("extensions"), "retry_policy.extensions")):
        ext = obj(extension, f"retry_policy.extensions[{index}]")
        count = ext.get("extra_reworks")
        valid = need(ext.get("stage") in STAGES, "retry extension stage is unknown")
        valid = need(type(count) is int and count > 0, "extra_reworks must be a positive integer") and valid
        valid = need(nonempty(ext.get("authorization")), "retry extension needs user authorization evidence") and valid
        if valid:
            extension_key = (ext["stage"], count, ext["authorization"])
            if need(extension_key not in extension_keys, "retry authorization is duplicated; do not copy prior extensions"):
                limits[ext["stage"]] += count
                extension_keys.add(extension_key)

    stages = obj(record.get("stages"), "stages")
    need(set(stages) == set(STAGES), "stages must contain exactly the eight production stages")
    previous_passed = True
    previous_outputs = sources
    next_stage = None
    last_passed_identity_image = set()
    for stage_index, (name, required_ids) in enumerate(STAGES.items()):
        stage = obj(stages.get(name), "stages." + name)
        status = stage.get("status")
        need(status in ("pending", "in_progress", "passed", "blocked"), name + ": invalid status")
        attempts = items(stage.get("attempts"), name + ".attempts")
        if name == "references" and (attempts or status == "passed") and not characters:
            need(nonempty(absence), "identity.absence_reason is required for a scene without characters")
        checks_needed = items(stage.get("required_checks"), name + ".required_checks")
        need(all(nonempty(x) for x in checks_needed), name + ": required check IDs must be strings")
        need(all(x in checks_needed for x in required_ids), name + ": missing mandatory check IDs")
        if not previous_passed:
            need(status == "pending" and not attempts, name + ": a preceding stage has not passed")
        if stage_index > stop_index:
            need(status == "pending" and not attempts, name + ": work exceeds task.stop_after_stage")
        if stage_index <= stop_index and status != "passed" and next_stage is None:
            next_stage = name
        if status == "blocked":
            blockers.append(name + ": stage explicitly blocked")
        if status == "pending":
            need(not attempts, name + ": pending stage cannot contain attempts")
        if status == "passed":
            need(bool(attempts), name + ": passed stage needs an attempt")
        used_attempts = history_counts[name] + len(attempts)
        need(used_attempts <= limits[name], name + ": retry limit exceeded without authorization")
        if stage_index <= stop_index and status != "passed" and not attempts and history_counts[name] >= limits[name]:
            blockers.append(name + ": previous records exhausted the automatic rework budget")
        if name == "brief" and status == "passed":
            need(bool(sources), "brief: source fingerprints are required")
            need(bool(constraints.get("locked")) and bool(constraints.get("allowed_changes")), "brief: locked constraints and allowed changes are required")
            need(not constraints.get("uncertainties"), "brief: unresolved uncertainties cannot pass")
        stage_identity_image = set()
        for index, raw_attempt in enumerate(attempts):
            loc = f"{name}.attempts[{index}]"
            attempt = obj(raw_attempt, loc)
            need(attempt.get("id") == f"{name}-{index + 1:02d}", loc + ": attempt ID must follow stage-NN order")
            need(attempt.get("kind") in ("plan", "image", "verification"), loc + ": invalid kind")
            if name in ("brief", "references", "composition", "space"):
                need(attempt.get("kind") != "image", loc + ": image generation is not allowed before sketch")
            for field in ("producer", "tool"):
                need(nonempty(attempt.get(field)), loc + "." + field + " is required")
            need(isinstance(attempt.get("prompt"), str), loc + ".prompt must be a string")
            if attempt.get("kind") == "image":
                need(nonempty(attempt.get("prompt")), loc + ": image attempt requires the exact prompt")
            if index:
                fix = obj(attempt.get("rework"), loc + ".rework")
                need(fix.get("from_attempt") == f"{name}-{index:02d}", loc + ": rework must refer to the previous attempt")
                for field in ("change", "preserve"):
                    need(nonempty(fix.get(field)), loc + ".rework." + field + " is required")
                finding_ids = items(fix.get("finding_ids"), loc + ".rework.finding_ids")
                previous = attempts[index - 1]
                previous_review = previous.get("review") if isinstance(previous, dict) else None
                prior_findings = previous_review.get("findings", []) if isinstance(previous_review, dict) else []
                prior_ids = [x.get("id") for x in prior_findings if isinstance(x, dict)] if isinstance(prior_findings, list) else []
                need(bool(finding_ids) and all(nonempty(x) and x in prior_ids for x in finding_ids), loc + ": rework needs existing finding IDs")
            inputs = files(attempt.get("inputs"), loc + ".inputs", required=True)
            need(bool(signatures(inputs) & signatures(previous_outputs)), loc + ": inputs must include a current previous-stage output (brief: a source)")
            identity_input(attempt, inputs, loc)
            if name in STAGING_STAGES and characters:
                need(attempt.get("staging_sha256") == staging_sha256, loc + ": staging_sha256 must match the current staging plan")
                need(signatures(staging_evidence) <= signatures(inputs), loc + ": inputs must include all staging evidence")
            review = attempt.get("review")
            outputs = files(attempt.get("outputs"), loc + ".outputs", required=review is not None, output_owner=f"{name}-{index}")
            if review is None:
                need(index == len(attempts) - 1 and status == "in_progress", loc + ": unfinished attempt must be last and in_progress")
                continue
            review = obj(review, loc + ".review")
            need(nonempty(review.get("reviewer")), loc + ": reviewer identity is required")
            if name in IDENTITY_STAGES or (name == "space" and characters):
                need(review.get("reviewer") != attempt.get("producer"), loc + ": reviewer must be independent of producer")
            if name in STAGING_STAGES and characters:
                need(review.get("staging_sha256") == staging_sha256, loc + ": review.staging_sha256 must match the current staging plan")
            verdict = review.get("verdict")
            need(verdict in ("pass", "rework", "blocked"), loc + ": invalid review verdict")
            reviewed_ids = []
            review_evidence = []
            all_pass = True
            identity_result = None
            staging_result = None
            staging_check_evidence = []
            for ci, raw_check in enumerate(items(review.get("checks"), loc + ".review.checks")):
                check_loc = f"{loc}.review.checks[{ci}]"
                check = obj(raw_check, check_loc)
                cid, result = check.get("id"), check.get("result")
                need(nonempty(cid), check_loc + ": check ID is required")
                need(cid not in reviewed_ids, check_loc + ": duplicate check ID")
                reviewed_ids.append(cid)
                if cid == "identity":
                    identity_result = result
                if cid == "identity_basis" and characters:
                    need(result != "not_applicable", check_loc + ": character identity basis cannot be waived")
                need(result in ("pass", "fail", "unverified", "not_applicable"), check_loc + ": invalid result")
                need(nonempty(check.get("observation")), check_loc + ": observation/reason is required")
                check_evidence = files(check.get("evidence"), check_loc + ".evidence", required=True)
                review_evidence.extend(check_evidence)
                if cid == "staging":
                    staging_result = result
                    staging_check_evidence = check_evidence
                    if characters:
                        need(result != "not_applicable", check_loc + ": character staging cannot be waived")
                        need(signatures(staging_evidence) <= signatures(check_evidence), check_loc + ": staging evidence must include the current plan sources")
                        if result == "pass":
                            observations = obj(check.get("observations"), check_loc + ".observations")
                            for field in SCENE_STAGING_FIELDS:
                                need(nonempty(observations.get(field)), check_loc + ".observations." + field + " needs a concrete scene observation")
                    else:
                        need(result == "not_applicable", check_loc + ": staging without characters must be not_applicable")
                if result == "not_applicable":
                    need(cid in CONDITIONAL, check_loc + ": this check cannot be not_applicable")
                if result not in ("pass", "not_applicable"):
                    all_pass = False
            need(all(cid in reviewed_ids for cid in checks_needed), loc + ": review is missing required checks")
            if name in IDENTITY_STAGES:
                stage_identity_image = character_review(attempt, review, inputs, outputs, loc, identity_result, staging_result)
                if characters:
                    need(stage_identity_image <= signatures(staging_check_evidence),
                         loc + ": staging evidence must include the same current image reviewed for every character")
            hard_open = False
            for fi, raw_finding in enumerate(items(review.get("findings"), loc + ".review.findings")):
                floc = f"{loc}.review.findings[{fi}]"
                finding = obj(raw_finding, floc)
                for field in ("id", "problem", "required_change", "preserve"):
                    need(nonempty(finding.get(field)), floc + "." + field + " is required")
                need(finding.get("severity") in ("hard", "soft"), floc + ": invalid severity")
                need(finding.get("state") in ("open", "resolved", "accepted"), floc + ": invalid state")
                review_evidence.extend(files(finding.get("evidence"), floc + ".evidence", required=True))
                if finding.get("severity") == "hard" and finding.get("state") != "resolved":
                    hard_open = True
            if verdict == "pass":
                need(all_pass and not hard_open, loc + ": pass contradicts failed/unverified checks or unresolved hard findings")
            need(bool(signatures(review_evidence) & signatures(outputs)), loc + ": review evidence must include the current attempt output")
            if verdict == "rework":
                need(bool(review.get("findings")), loc + ": rework requires an actionable finding")
            if index < len(attempts) - 1:
                need(verdict == "rework", loc + ": only a rework verdict can be followed by another automatic attempt")
            if index == len(attempts) - 1:
                if status == "passed":
                    need(verdict == "pass", name + ": passed status needs a passing last review")
                if verdict == "blocked":
                    blockers.append(name + ": latest review is blocked")
                if verdict == "rework" and used_attempts >= limits[name]:
                    blockers.append(name + ": automatic rework budget exhausted; user decision required")
        if status == "passed" and name in IDENTITY_STAGES:
            last_passed_identity_image = stage_identity_image
        previous_passed = previous_passed and status == "passed"
        if attempts and isinstance(attempts[-1], dict):
            previous_outputs = attempts[-1].get("outputs", [])
        else:
            previous_outputs = []

    adoption = obj(record.get("adoption"), "adoption")
    need(adoption.get("status") in ("candidate", "confirmed"), "adoption.status must be candidate or confirmed")
    delivered = isinstance(stages.get("delivery"), dict) and stages["delivery"].get("status") == "passed"
    selected = files(adoption.get("selected"), "adoption.selected", required=delivered)
    if delivered and characters:
        delivery_attempts = stages["delivery"].get("attempts", [])
        final_review = delivery_attempts[-1].get("review", {}) if delivery_attempts and isinstance(delivery_attempts[-1], dict) else {}
        final_checks = final_review.get("character_checks", []) if isinstance(final_review, dict) else []
        final_images = [c.get("image") for c in final_checks if isinstance(c, dict)] if isinstance(final_checks, list) else []
        need(bool(final_images) and all(signatures(selected) == signatures([picture]) for picture in final_images),
             "selected assets must match every character's final identity-reviewed image")
    recorded_outputs = []
    for stage in stages.values():
        if isinstance(stage, dict) and stage.get("status") == "passed" and isinstance(stage.get("attempts"), list) and stage["attempts"]:
            attempt = stage["attempts"][-1]
            if isinstance(attempt, dict) and isinstance(attempt.get("outputs"), list):
                recorded_outputs.extend(attempt["outputs"])
    need(signatures(selected) <= signatures(recorded_outputs), "selected assets must originate from a current passed production output")
    spec_assets = []
    for si, raw_spec in enumerate(items(adoption.get("asset_specs"), "adoption.asset_specs")):
        spec = obj(raw_spec, f"adoption.asset_specs[{si}]")
        spec_assets.extend(files([spec.get("asset")], f"adoption.asset_specs[{si}].asset", required=True))
        for dimension in ("width", "height"):
            need(type(spec.get(dimension)) is int and spec[dimension] > 0, f"asset_specs[{si}].{dimension} must be positive")
        need(nonempty(spec.get("format")) and nonempty(spec.get("display_treatment")), f"asset_specs[{si}] needs actual format and display treatment")
    if delivered:
        need(signatures(spec_assets) == signatures(selected), "delivered selected assets need matching asset_specs")
    if adoption.get("status") == "confirmed":
        need(nonempty(adoption.get("authorization")), "confirmed adoption requires user authorization evidence")
    integration = obj(adoption.get("integration"), "adoption.integration")
    need(integration.get("status") in ("not_requested", "pending", "passed"), "invalid integration status")
    files(integration.get("evidence"), "adoption.integration.evidence", required=integration.get("status") == "passed")
    if integration.get("status") == "passed":
        need(isinstance(stages.get("preview"), dict) and stages["preview"].get("status") == "passed", "runtime verification cannot pass before preview")
        need(bool(selected), "runtime verification requires selected assets")
    if integration.get("status") != "not_requested":
        need(task.get("scope") == "integrate", "integration requires task.scope=integrate")
        need(nonempty(integration.get("authorization")), "integration requires explicit user authorization evidence")
        need(adoption.get("status") == "confirmed", "integration requires confirmed adoption")
    if delivered and task.get("scope") == "integrate":
        need(integration.get("status") == "passed", "integrate scope cannot finish before runtime verification")
    valid = not errors
    scope_complete = valid and not blockers and next_stage is None
    complete = scope_complete and stop_after == "delivery"
    action = "complete" if complete else "scope_complete" if scope_complete else "resolve_record_errors" if errors else "resolve_blocker" if blockers else "start_stage"
    if valid and not blockers and next_stage:
        current_attempts = stages[next_stage]["attempts"]
        if current_attempts:
            latest_review = current_attempts[-1].get("review")
            action = "finish_attempt_and_review" if latest_review is None else "finalize_stage" if latest_review["verdict"] == "pass" else "rework"
    return {"valid_record": valid, "scope_complete": scope_complete, "production_complete": complete,
            "next_stage": next_stage, "next_action": action, "can_continue": valid and not blockers and not scope_complete,
            "attempts_used_in_previous_records": history_counts, "staging_sha256": staging_sha256,
            "errors": errors, "blockers": blockers, "boundary": BOUNDARY}


def init_record(path, scene, request, project, stop_after="delivery"):
    template = Path(__file__).resolve().parents[1] / "assets" / "scene-record.template.json"
    record = json.loads(template.read_text(encoding="utf-8-sig"))
    record = copy.deepcopy(record)
    record["task"].update(scene_id=scene, request=request,
                          project_root=str(Path(project).resolve()), authorization=request,
                          stop_after_stage=stop_after)
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return {"created": str(target.resolve()), "next_stage": "brief", "boundary": BOUNDARY}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="Create an unstarted record; never overwrite")
    init.add_argument("record")
    init.add_argument("--scene", required=True)
    init.add_argument("--request", required=True)
    init.add_argument("--project", required=True)
    init.add_argument("--stop-after", choices=tuple(STAGES), default="delivery")
    for name in ("check", "status"):
        child = sub.add_parser(name, help="Read-only evidence/sequence check and next stage")
        child.add_argument("record")
    fp = sub.add_parser("fingerprint", help="Print path and hash, never file contents")
    fp.add_argument("path")
    fp.add_argument("--role", default="reference")
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            if not Path(args.project).is_dir():
                raise ValueError("--project must be an existing directory")
            if not args.scene.strip() or not args.request.strip():
                raise ValueError("--scene and --request cannot be empty")
            result = init_record(args.record, args.scene, args.request, args.project, args.stop_after)
        elif args.command == "fingerprint":
            result = fingerprint(args.path, args.role)
        else:
            record = json.loads(Path(args.record).read_text(encoding="utf-8-sig"))
            result = validate(record, args.record)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result.get("errors") or result.get("blockers") else 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"valid_record": False, "errors": [str(exc)], "boundary": BOUNDARY}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
