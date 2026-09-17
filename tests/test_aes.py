import unittest

from crypto_library.aes import encrypt_block


class AesTests(unittest.TestCase):
    KEY = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")

    def test_nist_full_round_vectors(self):
        # NIST AES_Core128.pdf, encryption examples, pages 1-6.
        vectors = (
            ("6bc1bee22e409f96e93d7e117393172a", "3ad77bb40d7a3660a89ecaf32466ef97"),
            ("ae2d8a571e03ac9c9eb76fac45af8e51", "f5d3d58503b9699de785895a96fdbaaf"),
            ("30c81c46a35ce411e5fbc1191a0a52ef", "43b1cd7f598ece23881b00e3ed030688"),
            ("f69f2445df4f9b17ad2b417be66c3710", "7b0c785e27e8ad3f8223207104725dd4"),
        )
        for plaintext, ciphertext in vectors:
            with self.subTest(plaintext=plaintext):
                self.assertEqual(encrypt_block(bytes.fromhex(plaintext), self.KEY).hex(), ciphertext)

    def test_every_reduced_round_uses_final_round_without_mixcolumns(self):
        # Published ShiftRow, MixColumn, KeyAddition states for rounds 2-9.
        # Source: NIST AES_Core128.pdf, pages 1-2 (first plaintext block).
        # Round key = MixColumn XOR KeyAddition. Our final state therefore
        # equals ShiftRow XOR MixColumn XOR KeyAddition, with no AES oracle.
        states = (
            ("89b5884ac05653032e389b21604d123c", "0f31e929319a3558aec9589339f04d87", "fdf37cdb4b0c8c1bf7fcd8e94aa9bbf8"),
            ("54fe6141b3b0eab968d310afd60d641e", "9151abe1e5541cfd014a713eda7e3134", "acd1ec9ca242e2c31f690f7ab704b90f"),
            ("912c76763af956dec0f2ce2ea93e98da", "4d25cb1eecf716467658c73b49bcc9e9", "a2616e5f44a54d39c029e20092b764e9"),
            ("3a06981e1ba543cfbaa99f124fefe363", "f89b35ec4e40724e025b00c734d7d81b", "2c4af31432c3efc9c8a9b87b252ecda7"),
            ("712e6c5c23d3bdfae8310ddd3fd6df21", "a0c563696fb884e44840bfbee1d32f0a", "cd4dc0137eb3ba1993b939ff2bd3bcf7"),
            ("bd6d1268f356657ddc66bad4f1e3f416", "ac394c731f8de8c76711b210253ddb33", "e26dbb7d40d22134e3b7fda26b9b077c"),
            ("98b5541009a9c5ff1114ea187f3cfd3a", "ab05b572c8eb2b92ec04e2fd7d21ec34", "41d7c6537d669140dd2f179d02acc51b"),
            ("8333f0afff15a6edc191b409770e815e", "1741a11891c991688c36386f23ad82aa", "bb36c7eb88334d49a4e7112e74f182c4"),
        )
        plaintext = bytes.fromhex("6bc1bee22e409f96e93d7e117393172a")
        for rounds, triple in enumerate(states, start=2):
            expected = bytes(a ^ b ^ c for a, b, c in zip(*(bytes.fromhex(s) for s in triple)))
            with self.subTest(rounds=rounds):
                self.assertEqual(encrypt_block(plaintext, self.KEY, rounds), expected)

    def test_rejects_invalid_block_and_key(self):
        for invalid in (b"", b"a" * 15, b"a" * 17):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    encrypt_block(invalid, self.KEY)
                with self.assertRaises(ValueError):
                    encrypt_block(bytes(16), invalid)
        for invalid in (None, "a" * 16, [0] * 16, bytearray(16)):
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    encrypt_block(invalid, self.KEY)
                with self.assertRaises(TypeError):
                    encrypt_block(bytes(16), invalid)

    def test_rejects_invalid_rounds(self):
        for rounds in (-1, 0, 1, 11):
            with self.subTest(rounds=rounds), self.assertRaises(ValueError):
                encrypt_block(bytes(16), self.KEY, rounds)
        for rounds in (True, False, 2.0, "2", None):
            with self.subTest(rounds=rounds), self.assertRaises(TypeError):
                encrypt_block(bytes(16), self.KEY, rounds)


if __name__ == "__main__":
    unittest.main()
