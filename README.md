# Cryptology

Cryptology coursework: small, tested Python implementations and worked mathematical exercises, organized by topic and week.

## Project structure

```text
crypto_library/                 Reusable algorithms
    __init__.py
    number_theory.py            Euclid's GCD algorithm
tests/                         Unit and command-line tests
    test_number_theory.py
    test_run_gcd.py
exercises/                     Weekly worked solutions
    week01-solutions.md
docs/                          Study plans and verification notes
    week01-plan.md
run_gcd.py                     GCD command-line entry point
```

Keep future reusable algorithms in `crypto_library/`, corresponding tests in `tests/`, and weekly work in `exercises/weekNN-solutions.md` and `docs/weekNN-plan.md`.

## Quick start

Requires Python 3.9 or newer. No third-party dependencies or installation step are needed. Run commands from the project root.

Run the tests:

```bash
python3 -m unittest discover -s tests -v
```

Compute a GCD:

```bash
python3 run_gcd.py 48 18
```

Expected output: `6`. Use `python3 run_gcd.py --help` for usage.

The implementation accepts arbitrary-precision integers, normalizes negative inputs, and returns a nonnegative result. It defines `gcd(0, 0)` as `0`. Tests include 500-bit arithmetic and comparisons against Python's `math.gcd`.

## Week 1

- [Worked solutions for exercises 2.1-2.7](exercises/week01-solutions.md)
- [Study plan, difficulty ratings, and verification](docs/week01-plan.md)

The solutions refer to *Cryptology - how to crack it*, Lars Ramkilde Knudsen, first edition (2018), printed page 23. Equivalence to the course's named *Cryptology in Essence* edition has not been confirmed; check the assigned questions before relying on the numbering.

These are study materials, not an official answer key. Follow your course's collaboration and submission rules.

## Further worked exercises

- [Exercise 2.12: Chinese Remainder Theorem proof and worked example](exercises/exercise-2.12.md)

## Public repository scope

Source PDFs, lecture slides, private notes, local agent logs, temporary output, and credentials are excluded. Obtain the textbook and course material through authorized sources. The local PDFs are not required to run the code or tests.
