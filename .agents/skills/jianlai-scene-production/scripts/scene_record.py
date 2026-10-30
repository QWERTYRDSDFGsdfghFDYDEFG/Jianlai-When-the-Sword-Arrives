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
    "composition": ("story_relation", "framing"),
    "space": ("layout", "grounding"),
    "sketch": ("identity", "anatomy", "continuity"),
    "color": ("structure_preserved", "palette_light"),
    "preview": ("actual_composite", "dialogue_safe_area"),
    "delivery": ("provenance", "adoption_scope"),
}
CONDITIONAL = {"identity_basis", "identity", "anatomy", "grounding",
               "actual_composite", "dialogue_safe_area"}
BOUNDARY = "Only record structure and file fingerprints are checked; visual quality and user approval are not established by this tool."


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
                    need(key not in seen_outputs or seen_outputs[key] == output_owner,
                         loc + " reuses a previous attempt output path; preserve immutable outputs")
                    seen_outputs[key] = output_owner
        return entries

    record = obj(record, "record")
    need(record.get("schema_version") == 1, "schema_version must be 1")
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
        need(cursor.get("schema_version") == 1, "previous record must use schema_version 1")
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
    for stage_index, (name, required_ids) in enumerate(STAGES.items()):
        stage = obj(stages.get(name), "stages." + name)
        status = stage.get("status")
        need(status in ("pending", "in_progress", "passed", "blocked"), name + ": invalid status")
        attempts = items(stage.get("attempts"), name + ".attempts")
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
            review = attempt.get("review")
            outputs = files(attempt.get("outputs"), loc + ".outputs", required=review is not None, output_owner=f"{name}-{index}")
            if review is None:
                need(index == len(attempts) - 1 and status == "in_progress", loc + ": unfinished attempt must be last and in_progress")
                continue
            review = obj(review, loc + ".review")
            need(nonempty(review.get("reviewer")), loc + ": reviewer identity is required")
            if name in ("sketch", "color", "preview"):
                need(review.get("reviewer") != attempt.get("producer"), loc + ": reviewer must be independent of producer")
            verdict = review.get("verdict")
            need(verdict in ("pass", "rework", "blocked"), loc + ": invalid review verdict")
            reviewed_ids = []
            review_evidence = []
            all_pass = True
            for ci, raw_check in enumerate(items(review.get("checks"), loc + ".review.checks")):
                check_loc = f"{loc}.review.checks[{ci}]"
                check = obj(raw_check, check_loc)
                cid, result = check.get("id"), check.get("result")
                need(nonempty(cid), check_loc + ": check ID is required")
                need(cid not in reviewed_ids, check_loc + ": duplicate check ID")
                reviewed_ids.append(cid)
                need(result in ("pass", "fail", "unverified", "not_applicable"), check_loc + ": invalid result")
                need(nonempty(check.get("observation")), check_loc + ": observation/reason is required")
                review_evidence.extend(files(check.get("evidence"), check_loc + ".evidence", required=True))
                if result == "not_applicable":
                    need(cid in CONDITIONAL, check_loc + ": this check cannot be not_applicable")
                if result not in ("pass", "not_applicable"):
                    all_pass = False
            need(all(cid in reviewed_ids for cid in checks_needed), loc + ": review is missing required checks")
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
        previous_passed = previous_passed and status == "passed"
        if attempts and isinstance(attempts[-1], dict):
            previous_outputs = attempts[-1].get("outputs", [])
        else:
            previous_outputs = []

    adoption = obj(record.get("adoption"), "adoption")
    need(adoption.get("status") in ("candidate", "confirmed"), "adoption.status must be candidate or confirmed")
    delivered = isinstance(stages.get("delivery"), dict) and stages["delivery"].get("status") == "passed"
    selected = files(adoption.get("selected"), "adoption.selected", required=delivered)
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
            "attempts_used_in_previous_records": history_counts,
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
