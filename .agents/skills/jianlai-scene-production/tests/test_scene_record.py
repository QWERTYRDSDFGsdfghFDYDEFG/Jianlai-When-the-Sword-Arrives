"""Behavioral tests with in-memory fixtures; no test files are created."""
import contextlib
import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import unittest
from unittest import mock

sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("scene_record", SKILL / "scripts" / "scene_record.py")
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


TEMPLATE_PATH = SKILL / "assets" / "scene-record.template.json"
TEMPLATE_BYTES = TEMPLATE_PATH.read_bytes()
VISUAL_STAGES = {"sketch", "color", "preview", "delivery"}
STAGING_STAGES = {"composition", "space", *VISUAL_STAGES}
PLACEMENT_FIELDS = ("position", "footing", "facing", "gaze", "scale_depth", "occlusion")


class MemoryFiles:
    """Simulate command IO, including real SHA256 calculation and exclusive init."""

    def __init__(self):
        self.files = {}
        self.directories = set()

    @staticmethod
    def absolute(path):
        return Path(os.path.abspath(os.fspath(path)))

    def key(self, path):
        value = str(self.absolute(path))
        return value.casefold() if os.name == "nt" else value

    def add_directory(self, path):
        path = self.absolute(path)
        self.directories.update(self.key(parent) for parent in (path, *path.parents))

    def put(self, path, data):
        if self.key(Path(path).parent) not in self.directories:
            raise FileNotFoundError(str(Path(path).parent))
        self.files[self.key(path)] = data

    def read_bytes(self, path):
        try:
            return self.files[self.key(path)]
        except KeyError:
            raise FileNotFoundError(str(path)) from None

    def read_text(self, path, encoding=None, errors=None, **kwargs):
        return self.read_bytes(path).decode(encoding or "utf-8", errors or "strict")

    def write_bytes(self, path, data):
        self.put(path, bytes(data))
        return len(data)

    def write_text(self, path, data, encoding=None, errors=None, newline=None):
        self.put(path, data.encode(encoding or "utf-8", errors or "strict"))
        return len(data)

    def resolve(self, path, strict=False):
        if strict and not self.exists(path):
            raise FileNotFoundError(str(path))
        return self.absolute(path)

    def exists(self, path, **kwargs):
        key = self.key(path)
        return key in self.files or key in self.directories

    def mkdir(self, path, mode=0o777, parents=False, exist_ok=False):
        if self.exists(path) and not (exist_ok and self.key(path) in self.directories):
            raise FileExistsError(str(path))
        if not parents and self.key(Path(path).parent) not in self.directories:
            raise FileNotFoundError(str(Path(path).parent))
        self.add_directory(path)

    @contextlib.contextmanager
    def open(self, path, mode="r", buffering=-1, encoding=None, errors=None, newline=None):
        writable = any(flag in mode for flag in "wax+")
        if "x" in mode and self.exists(path):
            raise FileExistsError(str(path))
        if "w" in mode or "x" in mode:
            self.put(path, b"")
        data = self.read_bytes(path)
        stream = io.BytesIO(data) if "b" in mode else io.StringIO(data.decode(encoding or "utf-8", errors or "strict"), newline=newline)
        if "a" in mode:
            stream.seek(0, io.SEEK_END)
        try:
            yield stream
        finally:
            if writable:
                value = stream.getvalue()
                self.put(path, value if isinstance(value, bytes) else value.encode(encoding or "utf-8", errors or "strict"))
            stream.close()

    def install(self, test):
        methods = {
            "open": self.open, "read_bytes": self.read_bytes, "read_text": self.read_text,
            "write_bytes": self.write_bytes, "write_text": self.write_text,
            "resolve": self.resolve, "exists": self.exists, "mkdir": self.mkdir,
            "is_file": lambda path, **kwargs: self.key(path) in self.files,
            "is_dir": lambda path, **kwargs: self.key(path) in self.directories,
        }
        for name, handler in methods.items():
            patcher = mock.patch.object(Path, name, new=lambda path, *args, _handler=handler, **kwargs: _handler(path, *args, **kwargs))
            patcher.start()
            test.addCleanup(patcher.stop)
        for target in ("builtins.open", "io.open", "os.open"):
            patcher = mock.patch(target, side_effect=AssertionError("Real filesystem IO is forbidden in tests"))
            patcher.start()
            test.addCleanup(patcher.stop)


class SceneRecordTests(unittest.TestCase):
    def setUp(self):
        self.work = SKILL / "__memory_tests__" / self._testMethodName
        self.path = self.work / "record.json"
        self.fs = MemoryFiles()
        self.fs.add_directory(self.work)
        self.fs.add_directory(TEMPLATE_PATH.parent)
        self.fs.put(TEMPLATE_PATH, TEMPLATE_BYTES)
        self.fs.install(self)
        self.record = json.loads(TEMPLATE_BYTES)
        self.record["task"].update(scene_id="c2_example", request="Make the approved scene", project_root=str(self.work), authorization="User authorized candidate production")
        self.record["identity"] = {"characters": [], "absence_reason": "An unoccupied landscape; no characters are depicted."}
        self.source = self.asset("source.txt", "confirmed scene and constraints")
        self.record["sources"] = [self.source]
        self.record["constraints"].update(locked=["same characters"], allowed_changes=["lighting"])

    def asset(self, name, content="test-only evidence; not a visual judgement"):
        path = self.work / name
        path.write_text(content, encoding="utf-8")
        return tool.fingerprint(path, "test fixture")

    def attempt(self, stage, number=1, verdict="pass"):
        output = self.asset(f"{stage}-{number:02d}.png" if stage in VISUAL_STAGES else f"{stage}-{number:02d}.txt")
        attempt = {"id": f"{stage}-{number:02d}", "kind": "plan", "producer": "maker", "tool": "fixture", "prompt": "", "inputs": [self.source], "outputs": [output], "review": {"reviewer": "independent-reviewer", "verdict": verdict, "checks": [{"id": cid, "result": "pass", "observation": "test observation", "evidence": [output]} for cid in tool.STAGES[stage]], "findings": []}}
        prior_index = list(tool.STAGES).index(stage) - 1
        if prior_index >= 0:
            previous = self.record["stages"][list(tool.STAGES)[prior_index]]["attempts"]
            if previous:
                attempt["inputs"] += previous[-1]["outputs"]
        characters = self.record["identity"]["characters"]
        attempt["inputs"].extend(person["face_master"] for person in characters)
        if stage in VISUAL_STAGES:
            attempt["review"]["character_checks"] = [
                {"character_id": person["id"], "result": "pass" if person["visibility"] == "visible" else "not_applicable",
                 "observation": "Synthetic review evidence; this test makes no actual visual judgement.",
                 "view": "Same-side profile compared at native size and magnified for inspection.",
                 "image": output, "evidence": [person["face_master"], output],
                 "comparisons": {"face_shape": "Jaw and chin contour compared.", "features": "Brow, nose and mouth placement compared.", "age": "The established age remains visible.", "hair": "Hairline and silhouette compared."},
                 "placement": {"result": "pass", "observation": "The character was checked against the scene staging plan.",
                               "observations": {"position": "The character occupies the planned side of the clear action space.",
                                                "footing": "Both feet connect to the planned dry stone surface.",
                                                "facing": "Chest and hips face the planned action target.",
                                                "gaze": "The head and visible eye line track the action target.",
                                                "scale_depth": "Body size agrees with the planned depth and companions.",
                                                "occlusion": "The planned overlaps preserve the character silhouette."}}}
                for person in characters
            ]
        self.bind_staging(attempt)
        if verdict == "rework":
            attempt["review"]["checks"][0]["result"] = "fail"
            attempt["review"]["findings"] = [{"id": f"F{number}", "severity": "hard", "state": "open", "problem": "wrong direction", "required_change": "turn toward entrance", "preserve": "identity", "evidence": [output]}]
        if number > 1:
            attempt["rework"] = {"from_attempt": f"{stage}-{number-1:02d}", "finding_ids": [f"F{number-1}"], "change": "fix direction", "preserve": "identity"}
        return attempt

    def add_character(self, character_id="cpa", visibility="visible"):
        person = {"id": character_id, "face_master": self.asset(character_id + "-face.png", character_id + " face reference"),
                  "standard": self.asset(character_id + "-standard.txt", character_id + " identity standard"),
                  "visibility": visibility, "visibility_reason": "The full head faces away from the camera." if visibility == "not_visible" else ""}
        self.record["identity"]["characters"].append(person)
        self.record["identity"]["absence_reason"] = ""
        self.record["sources"].extend([person["face_master"], person["standard"]])
        plan = self.record.setdefault("staging", {})
        if not plan.get("characters"):
            evidence = self.asset("staging-source.txt", "Confirmed scene camera, ground landmarks, action space and character placements")
            self.record["sources"].append(evidence)
            plan.update(camera="View diagonally along the upper dry street from the river side.",
                        anchors="The stairs and retaining wall locate the lower quay; shops bound the upper street.",
                        action_target="The thrown object travels toward the cleared dry street, away from the waiting group.",
                        action_space="Reserve an unobstructed street area for the object to expand into the vessel.",
                        route="The companions can reach the future boarding side without crossing the vessel footprint.",
                        continuity="The action target and the next vessel reveal share the same cleared area and ground anchors.",
                        evidence=[evidence], characters=[])
        plan["characters"].append({"character_id": character_id,
                                   "position": "Behind the performer, offset from the other companions.",
                                   "footing": "Supported on the upper dry stone street, away from the stair opening.",
                                   "facing": "Torso and feet turn toward the cleared action area.",
                                   "gaze": "Look toward the thrown object and its destination.",
                                   "scale_depth": "Body size follows ground depth and the established companion proportions.",
                                   "occlusion": "Keep head, shoulder and action-bearing limbs legible."})
        return person

    def bind_staging(self, attempt):
        stage = attempt["id"].split("-")[0]
        if stage not in STAGING_STAGES:
            return
        review = attempt["review"]
        check = next(item for item in review["checks"] if item["id"] == "staging")
        if not self.record["identity"]["characters"]:
            check.update(result="not_applicable", observation="No characters are depicted in this landscape.")
            return
        plan = self.record["staging"]
        signature = tool.staging_digest(plan)
        attempt["staging_sha256"] = signature
        review["staging_sha256"] = signature
        for item in plan.get("evidence", []):
            if item not in attempt["inputs"]:
                attempt["inputs"].append(item)
        evidence = list(attempt["outputs"]) + list(plan.get("evidence", []))
        for person in review.get("character_checks", []):
            if person["image"] not in evidence:
                evidence.append(person["image"])
        check.update(result="pass", observation="Scene staging checked against the locked plan and current artifact.",
                     observations={"camera": "View and landmarks agree with the planned camera.",
                                   "action_target": "The action points toward the planned cleared ground.",
                                   "action_space": "The resulting vessel has a reserved footprint beyond the group.",
                                   "route": "The planned boarding approach remains open.",
                                   "continuity": "This view preserves the action location used by adjacent shots."},
                     evidence=evidence)

    def rebind_staging_record(self):
        for stage in STAGING_STAGES:
            for attempt in self.record["stages"][stage]["attempts"]:
                self.bind_staging(attempt)

    def generation(self, attempt):
        attempt.update(kind="image", prompt="Continue this scene while preserving each registered character identity.")
        paths = [item["path"] for item in attempt["inputs"] if Path(item["path"]).suffix == ".png"]
        attempt["identity_input"] = {"method": "reference_images", "call_id": "tool-event-" + attempt["id"],
                                     "arguments": {"prompt": attempt["prompt"], "referenced_image_paths": paths}}
        return attempt

    def people_scene(self, last="color"):
        self.add_character("cpa")
        self.add_character("pq")
        self.pass_through(last)
        return self.record["stages"][last]["attempts"][-1]

    def assert_valid(self):
        result = self.result()
        self.assertTrue(result["valid_record"], result["errors"])
        return result

    def pass_through(self, last):
        for name in tool.STAGES:
            self.record["stages"][name].update(status="passed", attempts=[self.attempt(name)])
            if name == last:
                break

    def result(self):
        return tool.validate(self.record, self.path)

    def cli(self, *args):
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            code = tool.main(list(args))
        return code, json.loads(capture.getvalue())

    def save(self):
        self.path.write_text(json.dumps(self.record), encoding="utf-8")

    def test_fresh_record_is_unfinished_and_read_only(self):
        self.save()
        before = self.path.read_bytes()
        code, result = self.cli("status", str(self.path))
        self.assertEqual(code, 0)
        self.assertTrue(result["valid_record"])
        self.assertFalse(result["production_complete"])
        self.assertEqual(result["next_stage"], "brief")
        self.assertEqual(before, self.path.read_bytes())

    def test_empty_pass_does_not_unlock_later_stage(self):
        self.record["stages"]["brief"]["status"] = "passed"
        self.assertFalse(self.result()["valid_record"])

    def test_preparation_scope_stops_before_image_generation(self):
        self.record["task"]["stop_after_stage"] = "space"
        self.pass_through("space")
        result = self.result()
        self.assertTrue(result["valid_record"])
        self.assertTrue(result["scope_complete"])
        self.assertFalse(result["production_complete"])
        self.assertFalse(result["can_continue"])
        self.assertIsNone(result["next_stage"])
        self.assertEqual(result["next_action"], "scope_complete")

    def test_sketch_only_scope_cannot_continue_to_color(self):
        self.record["task"]["stop_after_stage"] = "sketch"
        self.pass_through("sketch")
        self.assertTrue(self.result()["scope_complete"])
        self.assertFalse(self.result()["can_continue"])
        self.record["stages"]["color"].update(status="in_progress", attempts=[self.attempt("color")])
        self.assertFalse(self.result()["valid_record"])

    def test_invalid_stop_stage_and_integration_scope_mismatch(self):
        self.record["task"]["stop_after_stage"] = "unknown"
        self.assertFalse(self.result()["valid_record"])
        self.record["task"].update(scope="integrate", stop_after_stage="space")
        self.assertFalse(self.result()["valid_record"])

    def test_legacy_record_defaults_to_full_delivery(self):
        self.record["task"].pop("stop_after_stage", None)
        self.pass_through("space")
        self.assertTrue(self.result()["valid_record"])
        self.assertFalse(self.result()["scope_complete"])
        self.assertEqual(self.result()["next_stage"], "sketch")

    def test_init_preserves_explicit_stop_boundary(self):
        code, _ = self.cli("init", str(self.path), "--scene", "prep", "--request", "Only prepare before drawing", "--project", str(self.work), "--stop-after", "space")
        self.assertEqual(code, 0)
        initialized = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(initialized["task"]["stop_after_stage"], "space")

    def test_cannot_skip_to_color(self):
        self.record["stages"]["color"].update(status="passed", attempts=[self.attempt("color")])
        self.assertFalse(self.result()["valid_record"])

    def test_source_change_invalidates_previous_pass(self):
        self.pass_through("space")
        self.assertTrue(self.result()["valid_record"])
        Path(self.source["path"]).write_text("changed plot", encoding="utf-8")
        self.assertFalse(self.result()["valid_record"])
        self.assertEqual(self.result()["next_action"], "resolve_record_errors")

    def test_output_change_invalidates_review(self):
        self.pass_through("brief")
        output = self.record["stages"]["brief"]["attempts"][0]["outputs"][0]
        Path(output["path"]).write_text("changed after review", encoding="utf-8")
        self.assertFalse(self.result()["valid_record"])

    def test_same_maker_cannot_claim_independent_review(self):
        self.pass_through("sketch")
        self.record["stages"]["sketch"]["attempts"][0]["review"]["reviewer"] = "maker"
        self.assertFalse(self.result()["valid_record"])

    def test_planning_can_use_coordinator_review(self):
        self.pass_through("space")
        for name in ("brief", "references", "composition", "space"):
            self.record["stages"][name]["attempts"][0]["review"]["reviewer"] = "maker"
        self.assertTrue(self.result()["valid_record"])

    def test_generation_cannot_start_during_planning(self):
        self.pass_through("brief")
        self.record["stages"]["brief"]["attempts"][0].update(kind="image", prompt="generate now")
        self.assertFalse(self.result()["valid_record"])

    def test_unrelated_input_cannot_replace_previous_stage(self):
        self.pass_through("references")
        self.record["stages"]["references"]["attempts"][0]["inputs"] = [self.source]
        self.assertFalse(self.result()["valid_record"])

    def test_unrelated_review_evidence_is_rejected(self):
        self.pass_through("brief")
        for check in self.record["stages"]["brief"]["attempts"][0]["review"]["checks"]:
            check["evidence"] = [self.source]
        self.assertFalse(self.result()["valid_record"])

    def test_unverified_check_cannot_pass(self):
        self.pass_through("brief")
        self.record["stages"]["brief"]["attempts"][0]["review"]["checks"][0]["result"] = "unverified"
        self.assertFalse(self.result()["valid_record"])

    def test_nonconditional_check_cannot_be_waived(self):
        self.pass_through("brief")
        self.record["stages"]["brief"]["attempts"][0]["review"]["checks"][0]["result"] = "not_applicable"
        self.assertFalse(self.result()["valid_record"])

    def test_unresolved_hard_finding_cannot_be_accepted_as_pass(self):
        bad = self.attempt("brief", verdict="rework")
        bad["review"]["verdict"] = "pass"
        bad["review"]["checks"][0]["result"] = "pass"
        bad["review"]["findings"][0]["state"] = "accepted"
        self.record["stages"]["brief"].update(status="passed", attempts=[bad])
        self.assertFalse(self.result()["valid_record"])

    def test_retry_budget_stops_then_explicit_extension_resumes(self):
        stage = self.record["stages"]["brief"]
        stage.update(status="in_progress", attempts=[self.attempt("brief", i, "rework") for i in range(1, 4)])
        result = self.result()
        self.assertTrue(result["valid_record"])
        self.assertFalse(result["can_continue"])
        self.assertEqual(result["next_action"], "resolve_blocker")
        self.record["retry_policy"]["extensions"] = [{"stage": "brief", "extra_reworks": 1, "authorization": "User approved one further correction"}]
        self.assertTrue(self.result()["can_continue"])
        self.assertEqual(self.result()["next_action"], "rework")

    def test_fourth_attempt_needs_extension(self):
        self.record["stages"]["brief"].update(status="in_progress", attempts=[self.attempt("brief", i, "rework") for i in range(1, 5)])
        self.assertFalse(self.result()["valid_record"])

    def test_rework_must_point_to_actual_finding(self):
        attempts = [self.attempt("brief", 1, "rework"), self.attempt("brief", 2)]
        attempts[1]["rework"]["finding_ids"] = ["nonexistent"]
        self.record["stages"]["brief"].update(status="passed", attempts=attempts)
        self.assertFalse(self.result()["valid_record"])

    def test_reusing_attempt_output_path_is_rejected(self):
        attempts = [self.attempt("brief", 1, "rework"), self.attempt("brief", 2)]
        attempts[1]["outputs"] = copy.deepcopy(attempts[0]["outputs"])
        self.record["stages"]["brief"].update(status="passed", attempts=attempts)
        self.assertFalse(self.result()["valid_record"])

    def test_passing_review_needs_stage_finalization(self):
        self.record["stages"]["brief"].update(status="in_progress", attempts=[self.attempt("brief")])
        self.assertEqual(self.result()["next_action"], "finalize_stage")

    def test_candidate_completion_is_not_user_adoption(self):
        self.pass_through("delivery")
        self.record["adoption"]["selected"] = self.record["stages"]["color"]["attempts"][0]["outputs"]
        self.record["adoption"]["asset_specs"] = [{"asset": x, "width": 1672, "height": 941, "format": "fixture", "display_treatment": "synthetic metadata test only"} for x in self.record["adoption"]["selected"]]
        result = self.result()
        self.assertTrue(result["production_complete"])
        self.assertTrue(result["scope_complete"])
        self.assertEqual(result["next_action"], "complete")
        self.assertEqual(self.record["adoption"]["status"], "candidate")
        self.record["task"]["scope"] = "integrate"
        self.assertFalse(self.result()["production_complete"])

    def test_delivery_requires_asset_metadata_and_recorded_origin(self):
        self.pass_through("delivery")
        self.record["adoption"]["selected"] = [self.source]
        self.assertFalse(self.result()["valid_record"])
        self.record["adoption"]["selected"] = self.record["stages"]["color"]["attempts"][0]["outputs"]
        self.assertFalse(self.result()["valid_record"])

    def test_integration_requires_authority_and_runtime_evidence(self):
        self.record["task"]["scope"] = "integrate"
        self.record["adoption"]["status"] = "confirmed"
        self.record["adoption"]["authorization"] = "User selected final image"
        integration = self.record["adoption"]["integration"]
        integration["status"] = "passed"
        self.assertFalse(self.result()["valid_record"])
        integration.update(authorization="User authorized replacing this asset", evidence=[self.asset("runtime.txt")])
        self.assertFalse(self.result()["valid_record"])
        self.pass_through("preview")
        self.record["adoption"]["selected"] = self.record["stages"]["color"]["attempts"][0]["outputs"]
        self.assertTrue(self.result()["valid_record"])

    def test_discarded_attempt_cannot_be_selected(self):
        attempts = [self.attempt("brief", 1, "rework"), self.attempt("brief", 2)]
        self.record["stages"]["brief"].update(status="passed", attempts=attempts)
        self.record["adoption"]["selected"] = attempts[0]["outputs"]
        self.assertFalse(self.result()["valid_record"])

    def test_continuation_carries_retry_budget(self):
        self.record["stages"]["brief"].update(status="in_progress", attempts=[self.attempt("brief", i, "rework") for i in range(1, 4)])
        self.save()
        previous = tool.fingerprint(self.path, "previous record")
        self.path = self.work / "record-r2.json"
        self.record["previous_record"] = previous
        self.record["revision_reason"] = "Return to scene briefing"
        self.record["stages"]["brief"].update(status="pending", attempts=[])
        result = self.result()
        self.assertTrue(result["valid_record"])
        self.assertFalse(result["can_continue"])
        self.assertEqual(result["attempts_used_in_previous_records"]["brief"], 3)
        self.record["retry_policy"]["extensions"] = [{"stage": "brief", "extra_reworks": 1, "authorization": "User approved one more attempt after rollback"}]
        self.assertTrue(self.result()["can_continue"])

    def test_continuation_cycle_is_rejected(self):
        self.record["previous_record"] = {"path": str(self.path), "sha256": "0" * 64, "role": "previous"}
        self.record["revision_reason"] = "bad cycle"
        self.assertFalse(self.result()["valid_record"])

    def test_previous_authorization_cannot_be_counted_twice(self):
        self.record["retry_policy"]["extensions"] = [{"stage": "brief", "extra_reworks": 1, "authorization": "Same approval at T1"}]
        self.save()
        previous = tool.fingerprint(self.path, "previous")
        self.path = self.work / "record-r2.json"
        self.record["previous_record"] = previous
        self.record["revision_reason"] = "continue"
        self.assertFalse(self.result()["valid_record"])

    def test_init_refuses_overwrite(self):
        args = ("init", str(self.path), "--scene", "example", "--request", "Generate candidate", "--project", str(self.work))
        code, _ = self.cli(*args)
        self.assertEqual(code, 0)
        before = self.path.read_bytes()
        code, _ = self.cli(*args)
        self.assertEqual(code, 1)
        self.assertEqual(before, self.path.read_bytes())

    def test_malformed_json_and_types_are_reported(self):
        self.path.write_text("{", encoding="utf-8")
        self.assertEqual(self.cli("check", str(self.path))[0], 1)
        self.path.write_text("[]", encoding="utf-8")
        self.assertEqual(self.cli("check", str(self.path))[0], 1)
        self.record["retry_policy"]["extensions"] = [{"stage": []}]
        self.save()
        self.assertEqual(self.cli("check", str(self.path))[0], 1)

    def test_fingerprint_never_prints_contents(self):
        code, result = self.cli("fingerprint", self.source["path"])
        self.assertEqual(code, 0)
        self.assertEqual(set(result), {"path", "sha256", "role"})
        self.assertNotIn("confirmed scene and constraints", json.dumps(result))


    def test_initialization_uses_schema_two_and_empty_identity_register(self):
        code, _ = self.cli("init", str(self.path), "--scene", "example", "--request", "Prepare scene", "--project", str(self.work))
        self.assertEqual(code, 0)
        record = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(record["schema_version"], 2)
        self.assertEqual(record["identity"], {"characters": [], "absence_reason": ""})

    def test_identity_register_is_required_from_references(self):
        self.record["identity"]["absence_reason"] = ""
        self.pass_through("brief")
        self.assert_valid()
        self.record["stages"]["references"].update(status="in_progress", attempts=[self.attempt("references")])
        self.assertFalse(self.result()["valid_record"])

    def test_face_master_and_standard_must_be_registered_sources(self):
        self.people_scene()
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        person = self.record["identity"]["characters"][0]
        for field in ("face_master", "standard"):
            with self.subTest(field=field):
                self.record = copy.deepcopy(baseline)
                self.record["sources"].remove(person[field])
                self.assertFalse(self.result()["valid_record"])

    def test_color_requires_masters_in_inputs_and_actual_call(self):
        current = self.generation(self.people_scene())
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        master = self.record["identity"]["characters"][0]["face_master"]
        current["inputs"].remove(master)
        self.assertFalse(self.result()["valid_record"])
        self.record = baseline
        current = self.record["stages"]["color"]["attempts"][0]
        current["identity_input"]["arguments"]["referenced_image_paths"].remove(master["path"])
        self.assertFalse(self.result()["valid_record"])

    def test_later_color_revision_cannot_drop_master(self):
        self.people_scene("sketch")
        first = self.generation(self.attempt("color", verdict="rework"))
        second = self.generation(self.attempt("color", 2))
        self.record["stages"]["color"].update(status="passed", attempts=[first, second])
        self.assert_valid()
        second["identity_input"]["arguments"]["referenced_image_paths"].remove(self.record["identity"]["characters"][1]["face_master"]["path"])
        self.assertFalse(self.result()["valid_record"])

    def test_generation_request_needs_exact_prompt_and_event(self):
        self.generation(self.people_scene())
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        for field in ("prompt", "call_id"):
            with self.subTest(field=field):
                self.record = copy.deepcopy(baseline)
                payload = self.record["stages"]["color"]["attempts"][0]["identity_input"]
                if field == "prompt":
                    payload["arguments"]["prompt"] = "Different submitted request"
                else:
                    payload["call_id"] = ""
                self.assertFalse(self.result()["valid_record"])

    def test_pending_generation_can_register_before_tool_returns(self):
        self.people_scene("sketch")
        current = self.generation(self.attempt("color"))
        current["outputs"] = []
        current["review"] = None
        current["identity_input"]["call_id"] = ""
        self.record["stages"]["color"].update(status="in_progress", attempts=[current])
        self.assert_valid()
        self.assertEqual(self.result()["next_action"], "finish_attempt_and_review")

    def test_each_character_needs_one_review_not_an_overall_pass(self):
        self.people_scene()
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        for corruption in ("missing_one", "missing_all", "duplicate"):
            with self.subTest(corruption=corruption):
                self.record = copy.deepcopy(baseline)
                review = self.record["stages"]["color"]["attempts"][0]["review"]
                if corruption == "missing_one":
                    review["character_checks"].pop()
                elif corruption == "missing_all":
                    review.pop("character_checks")
                else:
                    review["character_checks"].append(copy.deepcopy(review["character_checks"][0]))
                self.assertFalse(self.result()["valid_record"])

    def test_character_review_must_compare_correct_master_and_current_image(self):
        self.generation(self.people_scene())
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        for corruption in ("wrong_master", "old_image", "text_as_image"):
            with self.subTest(corruption=corruption):
                self.record = copy.deepcopy(baseline)
                current = self.record["stages"]["color"]["attempts"][0]
                check = current["review"]["character_checks"][0]
                if corruption == "wrong_master":
                    check["evidence"][0] = self.record["identity"]["characters"][1]["face_master"]
                elif corruption == "old_image":
                    check["image"] = self.record["stages"]["sketch"]["attempts"][0]["outputs"][0]
                    check["evidence"][-1] = check["image"]
                else:
                    check["image"] = self.source
                    check["evidence"][-1] = self.source
                self.assertFalse(self.result()["valid_record"])

    def test_pass_requires_all_four_face_comparisons(self):
        current = self.people_scene()
        self.assert_valid()
        check = current["review"]["character_checks"][0]
        for field in ("face_shape", "features", "age", "hair"):
            with self.subTest(field=field):
                before = check["comparisons"][field]
                check["comparisons"][field] = ""
                self.assertFalse(self.result()["valid_record"])
                check["comparisons"][field] = before

    def test_small_unreadable_face_cannot_receive_overall_pass(self):
        current = self.people_scene()
        self.assert_valid()
        check = current["review"]["character_checks"][0]
        check.update(result="unverified", observation="The face is too small to resolve its landmarks.")
        self.assertFalse(self.result()["valid_record"])
        current["review"]["verdict"] = "blocked"
        next(item for item in current["review"]["checks"] if item["id"] == "identity")["result"] = "unverified"
        self.record["stages"]["color"]["status"] = "blocked"
        self.assert_valid()
        self.assertFalse(self.result()["can_continue"])

    def test_visible_identity_cannot_be_waived_globally_or_per_person(self):
        current = self.people_scene()
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        global_check = next(check for check in current["review"]["checks"] if check["id"] == "identity")
        global_check["result"] = "not_applicable"
        self.assertFalse(self.result()["valid_record"])
        self.record = baseline
        self.record["stages"]["color"]["attempts"][0]["review"]["character_checks"][0]["result"] = "not_applicable"
        self.assertFalse(self.result()["valid_record"])

    def test_hidden_face_requires_reason_and_may_be_not_applicable(self):
        self.add_character("cpa", visibility="not_visible")
        self.pass_through("preview")
        self.assert_valid()
        for name in ("sketch", "color", "preview"):
            review = self.record["stages"][name]["attempts"][0]["review"]
            next(check for check in review["checks"] if check["id"] == "identity")["result"] = "not_applicable"
        self.assert_valid()
        self.record["identity"]["characters"][0]["visibility_reason"] = ""
        self.assertFalse(self.result()["valid_record"])

    def test_empty_background_allows_identity_not_applicable(self):
        self.pass_through("preview")
        for name in ("sketch", "color", "preview"):
            review = self.record["stages"][name]["attempts"][0]["review"]
            next(check for check in review["checks"] if check["id"] == "identity")["result"] = "not_applicable"
        self.assert_valid()

    def test_preserved_pixels_needs_source_evidence_and_face_review(self):
        current = self.generation(self.people_scene())
        source_image = self.record["stages"]["sketch"]["attempts"][0]["outputs"][0]
        evidence = self.asset("pixel-write-report.txt", "Mock differential and in-place write evidence")
        current["identity_input"] = {"method": "preserved_pixels", "source": source_image, "evidence": [evidence]}
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        current["identity_input"]["evidence"] = []
        self.assertFalse(self.result()["valid_record"])
        self.record = baseline
        self.record["stages"]["color"]["attempts"][0]["review"].pop("character_checks")
        self.assertFalse(self.result()["valid_record"])

    def test_delivery_requires_independent_identity_check_of_selected_image(self):
        current = self.people_scene("delivery")
        selected = current["outputs"]
        self.record["adoption"]["selected"] = selected
        self.record["adoption"]["asset_specs"] = [{"asset": selected[0], "width": 1672, "height": 941, "format": "fixture", "display_treatment": "Synthetic fixture only"}]
        self.assertTrue(self.assert_valid()["production_complete"])
        current["review"]["reviewer"] = "maker"
        self.assertFalse(self.result()["valid_record"])
        current["review"]["reviewer"] = "independent-reviewer"
        earlier = self.record["stages"]["color"]["attempts"][0]["outputs"]
        self.record["adoption"]["selected"] = earlier
        self.record["adoption"]["asset_specs"][0]["asset"] = earlier[0]
        self.assertFalse(self.result()["valid_record"])

    def test_legacy_schema_one_is_read_only_and_cannot_continue(self):
        self.record["schema_version"] = 1
        self.record.pop("identity")
        self.save()
        before = self.path.read_bytes()
        code, result = self.cli("status", str(self.path))
        self.assertEqual(code, 1)
        self.assertFalse(result["can_continue"])
        self.assertFalse(result["production_complete"])
        self.assertEqual(before, self.path.read_bytes())

    def test_legacy_history_still_consumes_retry_budget(self):
        self.record["stages"]["brief"].update(status="in_progress", attempts=[self.attempt("brief", i, "rework") for i in range(1, 4)])
        self.record["schema_version"] = 1
        self.record.pop("identity")
        self.save()
        previous = tool.fingerprint(self.path, "legacy production record")
        self.path = self.work / "record-r2.json"
        self.record["schema_version"] = 2
        self.record["identity"] = {"characters": [], "absence_reason": "No characters appear in this landscape."}
        self.record["previous_record"] = previous
        self.record["revision_reason"] = "Revalidate identity without resetting the automatic retry budget"
        self.record["stages"]["brief"].update(status="pending", attempts=[])
        result = self.assert_valid()
        self.assertEqual(result["attempts_used_in_previous_records"]["brief"], 3)
        self.assertFalse(result["can_continue"])


    def test_delivery_cannot_mix_selected_image_with_older_character_review(self):
        current = self.people_scene("delivery")
        selected = current["outputs"]
        self.record["adoption"]["selected"] = selected
        self.record["adoption"]["asset_specs"] = [{"asset": selected[0], "width": 1672, "height": 941, "format": "fixture", "display_treatment": "Synthetic fixture only"}]
        self.assertTrue(self.assert_valid()["production_complete"])
        older = self.record["stages"]["color"]["attempts"][0]["outputs"][0]
        current["inputs"].append(older)
        second_person = current["review"]["character_checks"][1]
        second_person["image"] = older
        second_person["evidence"][-1] = older
        self.assertFalse(self.result()["valid_record"])

    def test_same_stage_cannot_mix_character_reviews_across_outputs(self):
        initial = copy.deepcopy(self.record)
        for stage in ("color", "preview"):
            with self.subTest(stage=stage):
                self.record = copy.deepcopy(initial)
                current = self.people_scene(stage)
                self.assert_valid()
                another_image = self.asset(stage + "-another.png", "A different complete scene")
                current["outputs"].append(another_image)
                second_person = current["review"]["character_checks"][1]
                second_person["image"] = another_image
                second_person["evidence"][-1] = another_image
                self.assertFalse(self.result()["valid_record"])

    def test_non_generation_output_cannot_be_replaced_by_reviewing_old_input(self):
        initial = copy.deepcopy(self.record)
        for kind in ("plan", "verification"):
            with self.subTest(kind=kind):
                self.record = copy.deepcopy(initial)
                current = self.people_scene()
                current["kind"] = kind
                self.assert_valid()
                older = self.record["stages"]["sketch"]["attempts"][0]["outputs"][0]
                self.assertIn(older, current["inputs"])
                for person in current["review"]["character_checks"]:
                    person["image"] = older
                    person["evidence"][-1] = older
                self.assertFalse(self.result()["valid_record"])


    def test_report_only_preview_and_delivery_use_latest_passed_image(self):
        self.people_scene()
        color_image = self.record["stages"]["color"]["attempts"][0]["outputs"][0]
        for stage in ("preview", "delivery"):
            current = self.attempt(stage)
            report = self.asset(stage + "-report.json", '{"inspection": "synthetic evidence"}')
            current["outputs"] = [report]
            if color_image not in current["inputs"]:
                current["inputs"].append(color_image)
            for check in current["review"]["checks"]:
                check["evidence"] = [report]
            for person in current["review"]["character_checks"]:
                person["image"] = color_image
                person["evidence"][-1] = color_image
            self.bind_staging(current)
            self.record["stages"][stage].update(status="passed", attempts=[current])
        self.record["adoption"]["selected"] = [color_image]
        self.record["adoption"]["asset_specs"] = [{"asset": color_image, "width": 1672, "height": 941, "format": "fixture", "display_treatment": "Synthetic fixture only"}]
        self.assertTrue(self.assert_valid()["production_complete"])
        baseline = copy.deepcopy(self.record)
        older = self.record["stages"]["sketch"]["attempts"][0]["outputs"][0]
        for stage in ("preview", "delivery"):
            with self.subTest(stage=stage):
                self.record = copy.deepcopy(baseline)
                current = self.record["stages"][stage]["attempts"][0]
                current["inputs"].append(older)
                for person in current["review"]["character_checks"]:
                    person["image"] = older
                    person["evidence"][-1] = older
                self.assertFalse(self.result()["valid_record"])

    def test_cross_stage_output_reuse_requires_unchanged_fingerprint(self):
        current = self.people_scene()
        previous_image = self.record["stages"]["sketch"]["attempts"][0]["outputs"][0]
        current["outputs"] = [previous_image]
        for check in current["review"]["checks"]:
            check["evidence"] = [previous_image]
        for person in current["review"]["character_checks"]:
            person["image"] = previous_image
            person["evidence"][-1] = previous_image
        self.bind_staging(current)
        self.assert_valid()
        Path(previous_image["path"]).write_text("Altered scene bytes after the sketch review", encoding="utf-8")
        changed = tool.fingerprint(previous_image["path"], "changed current-stage image")
        current["outputs"] = [changed]
        for check in current["review"]["checks"]:
            check["evidence"] = [changed]
        for person in current["review"]["character_checks"]:
            person["image"] = changed
            person["evidence"][-1] = changed
        self.assertFalse(self.result()["valid_record"])


    def test_character_staging_can_be_empty_in_preparation_but_not_composition(self):
        self.add_character()
        self.record["staging"] = json.loads(TEMPLATE_BYTES)["staging"]
        self.pass_through("references")
        self.assert_valid()
        self.record["stages"]["composition"].update(status="passed", attempts=[self.attempt("composition")])
        self.assertFalse(self.result()["valid_record"])

    def test_staging_roster_must_match_every_registered_character_once(self):
        self.people_scene("composition")
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        for corruption in ("missing", "duplicate", "unknown"):
            with self.subTest(corruption=corruption):
                self.record = copy.deepcopy(baseline)
                entries = self.record["staging"]["characters"]
                if corruption == "missing":
                    entries.pop()
                elif corruption == "duplicate":
                    entries.append(copy.deepcopy(entries[0]))
                else:
                    entries[1]["character_id"] = "unregistered-person"
                self.rebind_staging_record()
                self.assertFalse(self.result()["valid_record"])

    def test_staging_needs_camera_anchors_action_space_route_and_continuity(self):
        self.people_scene("composition")
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        for field in ("camera", "anchors", "action_target", "action_space", "route", "continuity"):
            with self.subTest(field=field):
                self.record = copy.deepcopy(baseline)
                self.record["staging"][field] = ""
                self.rebind_staging_record()
                self.assertFalse(self.result()["valid_record"])

    def test_character_plan_cannot_be_only_a_footing_check(self):
        self.people_scene("space")
        self.assert_valid()
        entry = self.record["staging"]["characters"][0]
        for field in PLACEMENT_FIELDS:
            if field != "footing":
                entry[field] = ""
        self.rebind_staging_record()
        self.assertFalse(self.result()["valid_record"])

    def test_staging_plan_evidence_must_be_a_registered_source(self):
        self.people_scene("composition")
        self.assert_valid()
        self.record["sources"].remove(self.record["staging"]["evidence"][0])
        self.assertFalse(self.result()["valid_record"])

    def test_color_identity_pass_cannot_replace_character_placement_review(self):
        current = self.people_scene()
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        current["review"]["character_checks"][0].pop("placement")
        self.assertFalse(self.result()["valid_record"])
        for field in PLACEMENT_FIELDS:
            with self.subTest(field=field):
                self.record = copy.deepcopy(baseline)
                placement = self.record["stages"]["color"]["attempts"][0]["review"]["character_checks"][0]["placement"]
                placement["observations"][field] = ""
                self.assertFalse(self.result()["valid_record"])

    def test_failed_or_unverified_placement_blocks_even_when_identity_passes(self):
        self.people_scene()
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        for result in ("fail", "unverified"):
            with self.subTest(result=result):
                self.record = copy.deepcopy(baseline)
                current = self.record["stages"]["color"]["attempts"][0]
                current["review"]["character_checks"][0]["placement"].update(result=result, observation="The action target or ground support is unresolved.")
                self.assertFalse(self.result()["valid_record"])
                next(item for item in current["review"]["checks"] if item["id"] == "staging")["result"] = result
                current["review"]["verdict"] = "blocked"
                self.record["stages"]["color"]["status"] = "blocked"
                self.assert_valid()
                self.assertFalse(self.result()["can_continue"])

    def test_attempt_and_review_must_bind_the_current_staging_plan(self):
        self.people_scene()
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        for location in ("attempt", "review"):
            with self.subTest(location=location):
                self.record = copy.deepcopy(baseline)
                current = self.record["stages"]["color"]["attempts"][0]
                target = current if location == "attempt" else current["review"]
                target["staging_sha256"] = "0" * 64
                self.assertFalse(self.result()["valid_record"])

    def test_changing_staging_invalidates_prior_stage_signatures(self):
        self.people_scene()
        original = self.assert_valid()["staging_sha256"]
        self.record["staging"]["action_target"] = "A newly chosen dry area further along the street."
        result = self.result()
        self.assertFalse(result["valid_record"])
        self.assertFalse(result["can_continue"])
        self.assertNotEqual(result["staging_sha256"], original)
        self.assertEqual(result["staging_sha256"], tool.staging_digest(self.record["staging"]))

    def test_reordering_plan_keys_does_not_invalidate_staging(self):
        self.people_scene()
        original = self.assert_valid()["staging_sha256"]
        self.record["staging"] = dict(reversed(list(self.record["staging"].items())))
        self.assertEqual(self.assert_valid()["staging_sha256"], original)

    def test_later_revision_cannot_drop_staging_source_or_signature(self):
        self.people_scene("sketch")
        first = self.generation(self.attempt("color", verdict="rework"))
        second = self.generation(self.attempt("color", 2))
        self.record["stages"]["color"].update(status="passed", attempts=[first, second])
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        for missing in ("input", "attempt_signature", "review_signature"):
            with self.subTest(missing=missing):
                self.record = copy.deepcopy(baseline)
                current = self.record["stages"]["color"]["attempts"][-1]
                if missing == "input":
                    current["inputs"].remove(self.record["staging"]["evidence"][0])
                elif missing == "attempt_signature":
                    current.pop("staging_sha256")
                else:
                    current["review"].pop("staging_sha256")
                self.assertFalse(self.result()["valid_record"])

    def test_staging_review_needs_plan_evidence_and_current_image(self):
        self.people_scene()
        self.assert_valid()
        baseline = copy.deepcopy(self.record)
        for corruption in ("missing_plan", "old_image", "missing_observation"):
            with self.subTest(corruption=corruption):
                self.record = copy.deepcopy(baseline)
                current = self.record["stages"]["color"]["attempts"][0]
                check = next(item for item in current["review"]["checks"] if item["id"] == "staging")
                if corruption == "missing_plan":
                    check["evidence"] = list(current["outputs"])
                elif corruption == "old_image":
                    older = self.record["stages"]["sketch"]["attempts"][0]["outputs"][0]
                    check["evidence"] = list(self.record["staging"]["evidence"]) + [older]
                else:
                    check["observations"] = {"camera": "Camera checked; the remaining spatial relationships were not checked."}
                self.assertFalse(self.result()["valid_record"])

    def test_space_with_characters_requires_independent_review(self):
        current = self.people_scene("space")
        self.assert_valid()
        current["review"]["reviewer"] = current["producer"]
        self.assertFalse(self.result()["valid_record"])

    def test_hidden_face_does_not_waive_placement_or_global_staging(self):
        self.add_character(visibility="not_visible")
        self.pass_through("color")
        self.assert_valid()
        current = self.record["stages"]["color"]["attempts"][0]
        self.assertEqual(current["review"]["character_checks"][0]["result"], "not_applicable")
        placement = current["review"]["character_checks"][0]["placement"]
        placement["observations"]["footing"] = "Feet are outside this crop; visible body support is checked against the approved spatial plan."
        self.assert_valid()
        placement["result"] = "not_applicable"
        self.assertFalse(self.result()["valid_record"])
        placement["result"] = "pass"
        next(item for item in current["review"]["checks"] if item["id"] == "staging")["result"] = "not_applicable"
        self.assertFalse(self.result()["valid_record"])

    def test_empty_background_has_no_staging_digest_and_may_waive_staging(self):
        self.pass_through("preview")
        result = self.assert_valid()
        self.assertIsNone(result["staging_sha256"])
        for stage in ("composition", "space", "sketch", "color", "preview"):
            check = next(item for item in self.record["stages"][stage]["attempts"][0]["review"]["checks"] if item["id"] == "staging")
            self.assertEqual(check["result"], "not_applicable")


if __name__ == "__main__":
    unittest.main(verbosity=2)
