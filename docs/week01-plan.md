# Week 1 study plan

Work through [the week 1 solutions](../exercises/week01-solutions.md) one exercise at a time. Each gives concrete steps, an answer, and a short optional question. The original course target was Friday, 4 September 2026.

## Study in short sessions

| Session | Work | Suggested time |
| --- | --- | --- |
| 1 | 2.1 and 2.2: GCD and LCM | 15 minutes |
| 2 | 2.3, 2.4, and 2.5: primes and counterexamples | 20 minutes |
| 3 | 2.6 and 2.7: remainders and an inverse | 15 minutes |
| 4 | Run the GCD examples and checks | 10 minutes |

These times are estimates. Pause between sessions. Cover each answer and reproduce its calculation before moving on.

## What is complete

- Exercises 2.1 through 2.7 have worked solutions and runnable arithmetic checks.
- Exercise 2.3 now answers whether **31** is prime. The prior transcription incorrectly used 3.
- The GCD implementation uses Euclid's algorithm and Python integers, including signed, zero, and large inputs.
- The solutions explain the GCD loop with 48 and 18 and include a runnable example with 499-bit and 500-bit integers.

See the [source notes](../exercises/week01-solutions.md#source-notes) for the visually checked page and the edition caveat.

## Verify before class

Run these commands from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 run_gcd.py 1071 462
```

The tests should pass, and the second command prints `21`. The suite can grow as later weeks add algorithms, so no fixed test count is assumed here.

Run both Python blocks in the [solution document](../exercises/week01-solutions.md). The large-integer example prints `499 500` and `True`. The arithmetic block prints `All arithmetic checks passed.` Finite numerical checks supplement the general proofs.

Before you put the notes away, explain why replacing `(a, b)` with `(b, a % b)` preserves the common divisors. Then explain why the last nonzero remainder is the GCD.
