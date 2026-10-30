"""Behavioral tests; fixtures remain outside the repository, never auto-deleted."""
import contextlib
import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("scene_record", SKILL / "scripts" / "scene_record.py")
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


class SceneRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parent = os.environ.get("SCENE_RECORD_TEST_ROOT")
        cls.root = Path(tempfile.mkdtemp(prefix="scene_record_tests_", dir=parent))
        print("Retained test fixtures:", cls.root)

    def setUp(self):
        self.work = self.root / self._testMethodName
        self.work.mkdir()
        self.path = self.work / "record.json"
        self.record = json.loads((SKILL / "assets" / "scene-record.template.json").read_text(encoding="utf-8"))
        self.record["task"].update(scene_id="c2_example", request="Make the approved scene", project_root=str(self.work), authorization="User authorized candidate production")
        self.source = self.asset("source.txt", "confirmed scene and constraints")
        self.record["sources"] = [self.source]
        self.record["constraints"].update(locked=["same characters"], allowed_changes=["lighting"])

    def asset(self, name, content="test-only evidence; not a visual judgement"):
        path = self.work / name
        path.write_text(content, encoding="utf-8")
        return tool.fingerprint(path, "test fixture")

    def attempt(self, stage, number=1, verdict="pass"):
        output = self.asset(f"{stage}-{number:02d}.txt")
        attempt = {"id": f"{stage}-{number:02d}", "kind": "plan", "producer": "maker", "tool": "fixture", "prompt": "", "inputs": [self.source], "outputs": [output], "review": {"reviewer": "independent-reviewer", "verdict": verdict, "checks": [{"id": cid, "result": "pass", "observation": "test observation", "evidence": [output]} for cid in tool.STAGES[stage]], "findings": []}}
        prior_index = list(tool.STAGES).index(stage) - 1
        if prior_index >= 0:
            previous = self.record["stages"][list(tool.STAGES)[prior_index]]["attempts"]
            if previous:
                attempt["inputs"] += previous[-1]["outputs"]
        if verdict == "rework":
            attempt["review"]["checks"][0]["result"] = "fail"
            attempt["review"]["findings"] = [{"id": f"F{number}", "severity": "hard", "state": "open", "problem": "wrong direction", "required_change": "turn toward entrance", "preserve": "identity", "evidence": [output]}]
        if number > 1:
            attempt["rework"] = {"from_attempt": f"{stage}-{number-1:02d}", "finding_ids": [f"F{number-1}"], "change": "fix direction", "preserve": "identity"}
        return attempt

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
