# Encrypt your first AES block

We will encrypt a block, shorten the round count, and inspect how the bytes move.
Run the commands from the repository root. You only need Python 3.9 or newer.

This implementation is for coursework. Reduced rounds are nonstandard and unsafe for protecting data. This Python code is not a production cipher, including at 10 rounds. It uses data-dependent table lookups and branches, has no constant-time guarantee, and provides no authentication, padding, or message mode.

## 1. Get a result before reading the theory

Run this published NIST example.

```bash
python3 run_aes.py 6bc1bee22e409f96e93d7e117393172a 2b7e151628aed2a6abf7158809cf4f3c
```

You get this ciphertext.

```text
3ad77bb40d7a3660a89ecaf32466ef97
```

The first argument is the plaintext. The second is the key. Each pair of hex digits represents one byte, so each argument contains 16 bytes.

## 2. Try two rounds

Add `--rounds 2` to the same command.

```bash
python3 run_aes.py 6bc1bee22e409f96e93d7e117393172a 2b7e151628aed2a6abf7158809cf4f3c --rounds 2
```

The result changes.

```text
7b771db8bac0ea40770d1b5b1314e443
```

This exercise uses the following exact convention for `r` rounds.

1. XOR the plaintext with round key 0.
2. Run rounds 1 through `r-1` with SubBytes, ShiftRows, MixColumns, and AddRoundKey.
3. Run round `r` with SubBytes, ShiftRows, and AddRoundKey. Omit MixColumns.

The initial XOR is not counted as a round. The key schedule is the normal AES-128 schedule, truncated to the first `r+1` keys. The allowed range is 2 through 10. Only 10 gives standard AES-128. A reduced result is not the intermediate state after `r` full rounds of standard AES.

## 3. Arrange the bytes into columns

Open [the implementation](../crypto_library/aes.py) and find `encrypt_block`.
The state is a list of 16 byte values. A four-by-four grid helps you read that list.

For our plaintext, fill each column from top to bottom before moving right.

```text
6b  2e  e9  73
c1  40  3d  93
be  9f  7e  17
e2  96  11  2a
```

This is **column-major order**. The byte at row `r`, column `c` has list index `r + 4*c`.
Both row and column numbers start at zero.

Try locating `9f`. It is at row 2, column 1, so its index is `2 + 4*1 = 6`.

## 4. Follow the first round

Keep the same plaintext and key. The following checkpoints let you compare your hand calculation with [NIST's published trace](https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Standards-and-Guidelines/documents/examples/AES_Core128.pdf), pages 1–2.

1. **AddRoundKey.** XOR each byte with the corresponding key byte. The first byte becomes `6b XOR 2b = 40`.

   ```text
   40bfabf4 06ee4d30 42ca6b99 7a5c5816
   ```

2. **SubBytes.** Replace each byte using `S_BOX`. For example, `S_BOX[0x40] = 0x09`.

   ```text
   090862bf 6f28e304 2c747fee da4a6a47
   ```

3. **ShiftRows.** Move rows left by 0, 1, 2, and 3 places, wrapping around.

   ```text
   09287f47 6f746abf 2c4a6204 da08e3ee
   ```

4. **MixColumns.** Combine the four bytes within each column using finite-field arithmetic.

   ```text
   529f16c2 978615ca e01aae54 ba1a2659
   ```

5. **AddRoundKey.** XOR with round key 1, which is `a0fafe17 88542cb1 23a33939 2a6c7605`.

   ```text
   f265e8d5 1fd2397b c3b9976d 9076505c
   ```

These are complete states, printed column by column. A new round starts from the previous round's result.

For a small arithmetic check, look at the first MixColumns output byte.

```text
(02 * 09) XOR (03 * 28) XOR 7f XOR 47
= 12 XOR 78 XOR 7f XOR 47
= 52
```

Every value here is hexadecimal. Multiplication is in the AES field, not ordinary integer multiplication.
`_xtime` multiplies by `02`; multiplication by `03` is `_xtime(x) XOR x`.
When the shift overflows a byte, `_xtime` reduces modulo `0x11b`, representing `x^8 + x^4 + x^3 + x + 1`.

## 5. Follow the key schedule

Find `_round_keys`. Split the key into four consecutive four-byte words.
For each next word, XOR the word four positions earlier with the previous word.
Every fourth word first transforms that previous word.

Try the first transformation yourself.

```text
Last word of original key       09 cf 4f 3c
Rotate one byte left            cf 4f 3c 09
Replace each byte through S_BOX  8a 84 eb 01
XOR first byte with constant 01  8b 84 eb 01
XOR with first key word         2b 7e 15 16
First word of round key 1        a0 fa fe 17
```

Repeat the word rule to get the remaining words. The round constants begin `01, 02, 04, 08, 10, 20, 40, 80, 1b, 36`. `_xtime` generates them.

## 6. Call the function from Python

Run this block from your terminal.

```bash
python3 - <<'PY'
from crypto_library.aes import encrypt_block

plaintext = bytes.fromhex("6bc1bee22e409f96e93d7e117393172a")
key = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
print(encrypt_block(plaintext, key).hex())
PY
```

You get `3ad77bb40d7a3660a89ecaf32466ef97` again.
The function requires `bytes` inputs of exactly 16 bytes each. It rejects wrong types with `TypeError` and wrong sizes or round ranges with `ValueError`. Booleans are not round counts.

The code rebuilds the small key schedule on every call and processes one block at a time in Python. It favors readable steps over throughput. There is no hardware acceleration or bulk-message interface.

## 7. Check the implementation

Run the API and command-line checks.

```bash
python3 -m unittest discover -s tests -p '*aes.py' -v
```

The tests check four published 10-round vectors and every allowed reduced round count. They also check malformed inputs and command-line errors.

The reduced-round checks use three states published by NIST for each round.
They recover the round key as `MixColumn XOR KeyAddition`, then compute the expected result as `ShiftRow XOR round_key`.
These expected values do not call our AES implementation or its key expansion.
They verify our chosen reduced-round convention; they are not official NIST reduced-round AES vectors.

For the algorithm definition, consult [FIPS 197, updated 2023](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf), sections 3.4, 4.2, 5.1, and 5.2.
For the test inputs, ciphertexts, and intermediate states, consult [NIST's AES-128 core examples](https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Standards-and-Guidelines/documents/examples/AES_Core128.pdf), pages 1–6.
