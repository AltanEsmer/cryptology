import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "run_gcd.py"


class RunGcdTests(unittest.TestCase):
    def run_gcd(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_prints_gcd_of_positive_integers(self) -> None:
        result = self.run_gcd("48", "18")

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "6\n")

    def test_prints_non_negative_gcd_when_an_argument_is_negative(self) -> None:
        result = self.run_gcd("-48", "18")

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "6\n")

    def test_help_describes_the_gcd_calculation(self) -> None:
        result = self.run_gcd("--help")

        self.assertEqual(result.returncode, 0)
        self.assertIn(
            "Compute gcd(a, b) with Euclid's algorithm.",
            result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
