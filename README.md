# Cryptology

Worked course exercises and small Python implementations. The solutions use short calculations, explain why each step works, and finish with a check.

## Start studying

| Week | Worked solutions | Code to try |
|---|---|---|
| 1 | [Exercises 2.1–2.7](exercises/week01-solutions.md) | GCD and Python's large integers |
| 2 | [Exercises 2.8–2.12](exercises/week02-solutions.md) | Modular inverse, Euler's phi, Chinese Remainder Theorem |
| 3 | [Exercises 3.1, 3.3, 3.5, 3.6, and 3.8](exercises/week03-solutions.md) | [AES-128 walkthrough with 2–10 rounds](docs/aes-walkthrough.md) |

Try one exercise at a time. Follow the worked steps, hide the answer, and repeat the calculation yourself.

The assignment lists come from the local Fall 2026 week sheets. The textbook questions were visually checked in Lars Ramkilde Knudsen's *Cryptology - how to crack it*, first edition, 2018, stored locally as `cryptology_essence.pdf`. The course names *Cryptology in Essence*; equivalence between editions is unconfirmed. Each solution file identifies its printed and PDF pages.

Week 1 corrects an earlier transcription error. Exercise 2.3 asks whether **31** is prime.

## Run the examples

Use Python 3.9 or newer from the repository root. No installation or third-party packages are needed.

```bash
python3 run_gcd.py 48 18
```

This prints `6`.

```bash
python3 - <<'PY'
from crypto_library.number_theory import modular_inverse, euler_phi, chinese_remainder

print(modular_inverse(357, 1234))
print(euler_phi(491401))
print(chinese_remainder([5, 8], [7, 11]))
PY
```

This prints `1075`, `490700`, and `19` on separate lines.

Encrypt one 16-byte block with AES-128:

```bash
python3 run_aes.py 6bc1bee22e409f96e93d7e117393172a 2b7e151628aed2a6abf7158809cf4f3c
```

This prints `3ad77bb40d7a3660a89ecaf32466ef97`.

Add `--rounds 2` to experiment with two rounds. The implementation always starts with AddRoundKey and omits MixColumns in its selected final round. Only the 10-round setting is standard AES-128. The implementation is for learning, not protecting real data.

## Check your work

```bash
python3 -m unittest discover -s tests -v
```

The tests compare number theory with Python's arithmetic and direct counting, check AES against published NIST vectors, cover every supported reduced-round count, and exercise the command-line programs.

- [Week 1 study plan](docs/week01-plan.md) has short practice sessions and checks.
- [Exercise 2.12 in more detail](exercises/exercise-2.12.md) includes another CRT derivation.
- [Verification notes](docs/weeks01-03-verification.md) record the source checks, commands, and limitations.

## Project structure

- `crypto_library/` contains the reusable algorithms.
- `run_gcd.py` and `run_aes.py` provide command-line examples.
- `tests/` contains standard-library `unittest` checks.
- `exercises/` contains the weekly solutions.
- `docs/` contains study guidance and verification notes.

## Public repository scope

Source PDFs, lecture slides, private notes, local execution logs, temporary output, and credentials are excluded. Obtain the course material through authorized sources. No local PDFs are needed to run the code or tests.
