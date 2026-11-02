import tempfile
import unittest
from pathlib import Path

from andes_risk.core import make_synthetic_csv, load_observations, evaluate


class PipelineTest(unittest.TestCase):
    def test_synthetic_reproducibility(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / "a.csv", Path(tmp) / "b.csv"
            make_synthetic_csv(a, seed=42)
            make_synthetic_csv(b, seed=42)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            observations = load_observations(a)
            output = evaluate(observations)
            self.assertTrue(output["research_only"])
            self.assertLess(output["train_end_date"], output["test_start_date"])
            self.assertEqual(output["train_count"] + output["test_count"], 240)
            self.assertEqual(sum(output["confusion_matrix"].values()), output["test_count"])
            for metric in output["metrics"].values():
                self.assertGreaterEqual(metric, 0)
                self.assertLessEqual(metric, 1)

    def test_rejects_bad_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / "demo.csv"
            make_synthetic_csv(file)
            contents = file.read_text()
            file.write_text(contents.replace("SYNTHETIC_SITE", "", 1))
            with self.assertRaises(ValueError):
                load_observations(file)

    def test_minimum_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                make_synthetic_csv(Path(tmp) / "small.csv", n=20)


if __name__ == "__main__":
    unittest.main()
