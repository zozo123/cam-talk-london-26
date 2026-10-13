"""Behavioral invariants of the finite-world toy controller (stdlib only)."""
import unittest
from dataclasses import replace
from reference import (
    Admission, Branch, FiniteWorldScheduler, ForkGates, TrustedController,
    WorkCosts, admit, example_scheduler,
)


class AdmissionTests(unittest.TestCase):
    def setUp(self):
        self.g = ForkGates(True, True, True, True, True, True)
        self.c = WorkCosts(4, 7, 10, 1, 2, 5, 3, 2)

    def test_fork_if_all_gates_and_warm_comparison_win(self):
        self.assertEqual((self.c.warm, self.c.fork), (60, 53))
        self.assertEqual(admit(self.g, self.c), Admission.FORK)

    def test_no_fork_if_cache_is_better(self):
        self.assertEqual(admit(self.g, replace(self.c, warm_preparation=1)), Admission.USE_WARM)

    def test_security_failure_overrides_economic_gain(self):
        for field in vars(self.g):
            with self.subTest(field=field):
                self.assertEqual(admit(replace(self.g, **{field: False}), self.c), Admission.INADMISSIBLE)

    def test_invalid_costs(self):
        with self.assertRaises(ValueError):
            replace(self.c, restore=-1)


class SchedulingTests(unittest.TestCase):
    def test_identical_sibling_adds_no_coverage(self):
        s = example_scheduler()
        self.assertEqual(s.coverage({"family-A"}), s.coverage({"family-A", "family-A-clone"}))
        self.assertAlmostEqual(s.coverage({"family-A", "independent-C"}), 10 / 16)

    def test_failed_family_updates_correlated_conditional(self):
        s = example_scheduler()
        self.assertEqual(s.choose_next(), "family-A")
        s.record("family-A", "fail")
        self.assertEqual(s.predicted_pass("family-A-clone"), 0.0)
        self.assertAlmostEqual(s.predicted_pass("independent-C"), 0.4)
        self.assertEqual(s.choose_next(), "independent-C")

    def test_timeout_and_cancellation_not_failures(self):
        s = example_scheduler()
        s.record("family-A", "timeout")
        self.assertEqual(len(s.feasible), 16)
        self.assertAlmostEqual(s.predicted_pass("family-A-clone"), 6 / 16)
        s.record("independent-C", "cancelled")
        self.assertEqual(len(s.feasible), 16)
        self.assertEqual(s.events[-1], ("independent-C", "cancelled"))

    def test_stop_if_cost_exceeds_predicted_value(self):
        s = example_scheduler()
        self.assertIsNone(s.choose_next(cost_weight=1.0))

    def test_post_failure_replanning(self):
        s = example_scheduler()
        s.record("family-A", "fail")
        s.record("independent-C", "fail")
        self.assertAlmostEqual(s.predicted_pass("alternate-D"), 3 / 6)
        self.assertEqual(s.choose_next(), "alternate-D")

    def test_no_more_work_after_pass(self):
        s = example_scheduler()
        s.record("family-A", "pass")
        self.assertIsNone(s.choose_next())

    def test_duplicate_and_invalid_records(self):
        s = example_scheduler()
        s.record("family-A", "fail")
        with self.assertRaises(ValueError):
            s.record("family-A", "fail")
        with self.assertRaises(ValueError):
            s.record("family-A-clone", "maybe")

    def test_submodularity_exact_small_worlds(self):
        from itertools import combinations
        s = example_scheduler()
        names = set(s.branches)
        subsets = [set(t) for k in range(len(names)+1) for t in combinations(names, k)]
        for x in subsets:
            for y in subsets:
                if x <= y:
                    for j in names - y:
                        self.assertGreaterEqual(
                            s.coverage(x | {j}) - s.coverage(x),
                            s.coverage(y | {j}) - s.coverage(y) - 1e-12,
                        )


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.c = TrustedController("task-v1", "checker-v1", b"controller-side-secret")

    def test_exact_checked_bytes_only(self):
        receipt = self.c.check(b"good-patch", evaluation_id="eval-1", verifier=lambda b: b == b"good-patch")
        self.assertEqual(receipt.verdict, "pass")
        self.assertFalse(self.c.promote(b"different-bytes", receipt, expected_epoch=0))
        self.assertTrue(self.c.promote(b"good-patch", receipt, expected_epoch=0))
        self.assertFalse(self.c.promote(b"good-patch", receipt, expected_epoch=0))

    def test_no_duplicate_evaluation_token(self):
        self.c.check(b"x", evaluation_id="eval-1", verifier=lambda _: True)
        with self.assertRaises(ValueError):
            self.c.check(b"x", evaluation_id="eval-1", verifier=lambda _: True)

    def test_verifier_failure_cannot_promote(self):
        r = self.c.check(b"bad", evaluation_id="eval-1", verifier=lambda _: False)
        self.assertFalse(self.c.promote(b"bad", r, expected_epoch=0))

    def test_stale_epoch_cannot_promote(self):
        r = self.c.check(b"good", evaluation_id="eval-1", verifier=lambda _: True)
        self.c.next_epoch()
        self.assertFalse(self.c.promote(b"good", r, expected_epoch=0))
        self.assertFalse(self.c.promote(b"good", r, expected_epoch=1))

    def test_tampered_receipt_cannot_promote(self):
        r = self.c.check(b"good", evaluation_id="eval-1", verifier=lambda _: True)
        self.assertFalse(self.c.promote(b"good", replace(r, verifier_digest="evil"), expected_epoch=0))
        self.assertFalse(self.c.promote(b"good", replace(r, artifact_digest="evil"), expected_epoch=0))
        self.assertFalse(self.c.promote(b"good", replace(r, verdict="pass", mac="f"*64), expected_epoch=0))

    def test_incomplete_checker_pass_is_not_semantic_proof(self):
        # Deliberately weak oracle accepts a known-wrong patch, demonstrating limitation.
        r = self.c.check(b"WRONG", evaluation_id="eval-1", verifier=lambda _: True)
        self.assertEqual(r.verdict, "pass")
        self.assertTrue(self.c.promote(b"WRONG", r, expected_epoch=0))
        # The controller guarantees receipt/artifact binding, NOT test completeness.

    def test_verifier_exception_is_not_a_pass(self):
        def broken(_):
            raise RuntimeError("checker crashed")
        r = self.c.check(b"x", evaluation_id="eval-1", verifier=broken)
        self.assertEqual(r.verdict, "error")
        self.assertFalse(self.c.promote(b"x", r, expected_epoch=0))


if __name__ == "__main__":
    unittest.main(verbosity=2)