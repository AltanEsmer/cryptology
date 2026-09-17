# Weeks 1 to 3 verification

## Assignment coverage

| Week | Assigned written work covered | Implementation |
|---|---|---|
| 1 | 2.1–2.7, with 2.3 corrected from 3 to 31 | Existing Euclidean GCD explained and checked with 499-bit and 500-bit inputs |
| 2 | 2.8–2.12, including Wednesday's 2.12(1) proof | Modular inverse, Euler's phi, CRT |
| 3 | 3.1 with all four sheet hints; 3.3; all cipher variants in 3.5; every bullet in 3.6; both parts of 3.8 | AES-128 single-block encryption with 2–10 selectable rounds |

The local `week01.pdf`, `week02.pdf`, and `week03.pdf` supplied the assignment lists. Textbook statements were visually checked on printed pages 23–24 and 42–43, corresponding to PDF pages 13–14 and 23 of the local `cryptology_essence.pdf`.

The title and publication page identify *Cryptology - how to crack it*, Lars Ramkilde Knudsen, first edition, 2018. The course names *Cryptology in Essence*. Edition equivalence remains unconfirmed. The requested Downloads path was absent; the source used was the existing copy in the local course folder. No source PDFs or lecture material were added to this repository.

## Checks run

From the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q crypto_library run_aes.py run_gcd.py tests
git diff --check
```

The full suite passed **22 tests**. Compilation and whitespace checks passed. No formatter or linter is configured.

All **12 non-test bash examples** in the README, weekly solutions, AES walkthrough, and existing Exercise 2.12 solution were executed. Their output matched the documented results. These include all 4096 four-bit feedback combinations in the Exercise 3.8 inverse check and all 77 CRT reconstructions in the existing Exercise 2.12 check.

The number-theory tests compare modular inverses against Python's `pow(a, -1, modulus)`, phi values against direct coprime counting, and CRT outputs against the requested residues and canonical range. Invalid domains and types are checked. Existing GCD behavior remains covered.

AES tests compare four full-round blocks against [NIST's AES-128 examples](https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Standards-and-Guidelines/documents/examples/AES_Core128.pdf). Reduced-round expectations for rounds 2–9 derive from NIST's published intermediate states, independently of this implementation's key schedule. Those are checks of the documented reduced-round convention, not official NIST reduced-round vectors. The algorithm reference is [FIPS 197](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf).

## Limits

- Finite arithmetic checks support the worked examples. The general proofs remain necessary.
- Key-uniqueness estimates in Exercises 3.5 and 3.6 use the question's random-cipher approximation. They distinguish expected wrong keys from the guaranteed real key.
- Phi uses trial division, appropriate for these exercise inputs. It is not a practical factoring method for large cryptographic composites.
- The AES implementation encrypts one block. It has no decryption, padding, message mode, authentication, or constant-time guarantee. The week sheet requires encryption with a selectable round count. Only 10 rounds is standard AES-128.

## Independent review

A separate gpt-6-astra reviewer checked the scanned exercise statements, mathematical answers, code, published NIST intermediate states, and tests. It found no actionable correctness or missing-scope issues. This was an independent review within one model family, not a cross-family review. Source-edition uncertainty remains as described above.
