"""Educational AES-128 block encryption. Not a production cryptography library."""


# FIPS 197, Table 4. Row = high hex digit, column = low hex digit.
S_BOX = bytes.fromhex(
    "63 7c 77 7b f2 6b 6f c5 30 01 67 2b fe d7 ab 76"
    "ca 82 c9 7d fa 59 47 f0 ad d4 a2 af 9c a4 72 c0"
    "b7 fd 93 26 36 3f f7 cc 34 a5 e5 f1 71 d8 31 15"
    "04 c7 23 c3 18 96 05 9a 07 12 80 e2 eb 27 b2 75"
    "09 83 2c 1a 1b 6e 5a a0 52 3b d6 b3 29 e3 2f 84"
    "53 d1 00 ed 20 fc b1 5b 6a cb be 39 4a 4c 58 cf"
    "d0 ef aa fb 43 4d 33 85 45 f9 02 7f 50 3c 9f a8"
    "51 a3 40 8f 92 9d 38 f5 bc b6 da 21 10 ff f3 d2"
    "cd 0c 13 ec 5f 97 44 17 c4 a7 7e 3d 64 5d 19 73"
    "60 81 4f dc 22 2a 90 88 46 ee b8 14 de 5e 0b db"
    "e0 32 3a 0a 49 06 24 5c c2 d3 ac 62 91 95 e4 79"
    "e7 c8 37 6d 8d d5 4e a9 6c 56 f4 ea 65 7a ae 08"
    "ba 78 25 2e 1c a6 b4 c6 e8 dd 74 1f 4b bd 8b 8a"
    "70 3e b5 66 48 03 f6 0e 61 35 57 b9 86 c1 1d 9e"
    "e1 f8 98 11 69 d9 8e 94 9b 1e 87 e9 ce 55 28 df"
    "8c a1 89 0d bf e6 42 68 41 99 2d 0f b0 54 bb 16"
)


def _xtime(value: int) -> int:
    """Multiply a byte by x in GF(2^8), modulo x^8+x^4+x^3+x+1."""
    return ((value << 1) ^ (0x11B if value & 0x80 else 0)) & 0xFF


def _round_keys(key: bytes, rounds: int) -> list[list[int]]:
    """Expand the key into the first rounds+1 AES-128 round keys."""
    words = [list(key[i:i + 4]) for i in range(0, 16, 4)]
    round_constant = 1
    for i in range(4, 4 * (rounds + 1)):
        previous = words[i - 1][:]
        if i % 4 == 0:
            previous = previous[1:] + previous[:1]
            previous = [S_BOX[value] for value in previous]
            previous[0] ^= round_constant
            round_constant = _xtime(round_constant)
        words.append([a ^ b for a, b in zip(words[i - 4], previous)])
    return [sum(words[i:i + 4], []) for i in range(0, len(words), 4)]


def _mix_columns(state: list[int]) -> list[int]:
    """Mix each column using the AES matrix with entries 1, 2, and 3."""
    mixed = []
    for i in range(0, 16, 4):
        a, b, c, d = state[i:i + 4]
        a2, b2, c2, d2 = (_xtime(value) for value in (a, b, c, d))
        mixed.extend((
            a2 ^ (b2 ^ b) ^ c ^ d,
            a ^ b2 ^ (c2 ^ c) ^ d,
            a ^ b ^ c2 ^ (d2 ^ d),
            (a2 ^ a) ^ b ^ c ^ d2,
        ))
    return mixed


def encrypt_block(plaintext: bytes, key: bytes, rounds: int = 10) -> bytes:
    """Encrypt 16 bytes with a 16-byte key and 2..10 rounds.

    Use initial AddRoundKey, then rounds-1 full rounds, then a final round
    without MixColumns. Only 10 rounds is standard AES-128. Reject non-bytes
    inputs or non-integer rounds with TypeError, invalid sizes/ranges with
    ValueError. Booleans are not accepted as round counts.
    """
    for name, value in (("plaintext", plaintext), ("key", key)):
        if not isinstance(value, bytes):
            raise TypeError(f"{name} must be bytes")
        if len(value) != 16:
            raise ValueError(f"{name} must contain exactly 16 bytes")
    if not isinstance(rounds, int) or isinstance(rounds, bool):
        raise TypeError("rounds must be an integer")
    if not 2 <= rounds <= 10:
        raise ValueError("rounds must be between 2 and 10")

    keys = _round_keys(key, rounds)
    state = [value ^ k for value, k in zip(plaintext, keys[0])]
    for round_number in range(1, rounds + 1):
        state = [S_BOX[value] for value in state]
        # Column-major index = row + 4*column. Shift row r left by r columns.
        state = [state[row + 4 * ((column + row) % 4)]
                 for column in range(4) for row in range(4)]
        if round_number != rounds:
            state = _mix_columns(state)
        state = [value ^ k for value, k in zip(state, keys[round_number])]
    return bytes(state)
