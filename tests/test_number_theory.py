import math
import unittest

from crypto_library.number_theory import gcd


class GcdTests(unittest.TestCase):
    def test_common_factor(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_coprime_numbers(self):
        self.assertEqual(gcd(35, 64), 1)

    def test_zero_inputs(self):
        self.assertEqual(gcd(0, 27), 27)
        self.assertEqual(gcd(27, 0), 27)
        self.assertEqual(gcd(0, 0), 0)

    def test_negative_inputs(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_large_integers(self):
        factor = (1 << 251) - 1
        a = factor * (1 << 249)
        b = factor * 3
        self.assertGreaterEqual(a.bit_length(), 500)
        self.assertEqual(gcd(a, b), factor)

    def test_matches_standard_library_oracle(self):
        cases = (
            (391, 299),
            (2**127 - 1, 2**61 - 1),
            (-1234567890, 987654321),
        )
        for a, b in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(gcd(a, b), math.gcd(a, b))


if __name__ == "__main__":
    unittest.main()
