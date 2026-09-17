import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class RunAesTests(unittest.TestCase):
    BLOCK = "6bc1bee22e409f96e93d7e117393172a"
    KEY = "2b7e151628aed2a6abf7158809cf4f3c"

    def run_aes(self, *arguments):
        return subprocess.run(
            [sys.executable, str(PROJECT_ROOT / "run_aes.py"), *arguments],
            cwd=PROJECT_ROOT, capture_output=True, text=True, check=False,
        )

    def test_full_rounds(self):
        result = self.run_aes(self.BLOCK, self.KEY)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "3ad77bb40d7a3660a89ecaf32466ef97\n")

    def test_two_rounds(self):
        result = self.run_aes(self.BLOCK, self.KEY, "--rounds", "2")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "7b771db8bac0ea40770d1b5b1314e443\n")

    def test_invalid_arguments_are_concise_errors(self):
        cases = (
            ("zz" * 16, self.KEY), ("00", self.KEY), (self.BLOCK, "00"),
            (self.BLOCK, self.KEY, "--rounds", "1"),
            (self.BLOCK, self.KEY, "--rounds", "11"),
            (self.BLOCK, self.KEY, "--rounds", "2.5"), (),
        )
        for arguments in cases:
            with self.subTest(arguments=arguments):
                result = self.run_aes(*arguments)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("error:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_help(self):
        result = self.run_aes("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("--rounds", result.stdout)
        self.assertIn("16-byte", result.stdout)


if __name__ == "__main__":
    unittest.main()
