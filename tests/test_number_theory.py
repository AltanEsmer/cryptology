import math
import unittest

from crypto_library.number_theory import (
    chinese_remainder, euler_phi, gcd, modular_inverse,
)


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


class WeekTwoTests(unittest.TestCase):
    def test_inverse_examples_and_oracle(self):
        self.assertEqual(modular_inverse(357, 1234), 1075)
        for modulus in range(2, 45):
            for a in range(-modulus, modulus + 1):
                if math.gcd(a, modulus) == 1:
                    self.assertEqual(modular_inverse(a, modulus), pow(a, -1, modulus))
                else:
                    with self.assertRaises(ValueError):
                        modular_inverse(a, modulus)
        a, modulus = (1 << 251) - 1, 1 << 257
        self.assertEqual(modular_inverse(a, modulus), pow(a, -1, modulus))

    def test_phi_examples_and_counting_oracle(self):
        cases = (
            (1, 1), (5, 4), (341, 300), (491401, 490700),
            (701, 700), (108, 36), (2**200, 2**199),
        )
        for n, expected in cases:
            self.assertEqual(euler_phi(n), expected)
        for n in range(1, 150):
            count = sum(math.gcd(k, n) == 1 for k in range(1, n + 1))
            self.assertEqual(euler_phi(n), count)

    def test_crt_examples_and_residues(self):
        self.assertEqual(chinese_remainder([3, 5], [11, 13]), 135)
        self.assertEqual(chinese_remainder([5, 8], [7, 11]), 19)
        self.assertEqual(chinese_remainder([2, 3, 2], [3, 5, 7]), 23)
        self.assertEqual(chinese_remainder([-1], [7]), 6)
        for a in range(-4, 5):
            for b in range(-6, 7):
                x = chinese_remainder([a, b], [4, 9])
                self.assertTrue(0 <= x < 36)
                self.assertEqual((x % 4, x % 9), (a % 4, b % 9))

    def test_invalid_domains(self):
        for modulus in (-2, 0, 1):
            with self.assertRaises(ValueError):
                modular_inverse(3, modulus)
        for n in (-5, 0):
            with self.assertRaises(ValueError):
                euler_phi(n)
        cases = (
            ([], []), ([1], []), ([1, 2], [4, 6]), ([1, 2], [7, 7]),
            ([0], [1]), ([0], [0]), ([0], [-2]),
        )
        for residues, moduli in cases:
            with self.assertRaises(ValueError):
                chinese_remainder(residues, moduli)

    def test_rejects_non_integer_values(self):
        for value in (True, 1.5, "3", None):
            operations = (
                lambda: modular_inverse(value, 7),
                lambda: modular_inverse(3, value),
                lambda: euler_phi(value),
                lambda: chinese_remainder([value], [7]),
                lambda: chinese_remainder([3], [value]),
            )
            for operation in operations:
                with self.assertRaises(TypeError):
                    operation()


if __name__ == "__main__":
    unittest.main()
