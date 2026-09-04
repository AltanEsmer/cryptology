# Week 1 study plan

## Scope and status

The Week 1 work consists of a GCD implementation supporting 100-500-bit integers or larger, and Chapter 2 exercises 2.1-2.7. The original target was Friday, 4 September 2026.

- Implementation: complete, using Euclid's algorithm and Python integers.
- Tests: nine unit/CLI tests covering ordinary, coprime, signed, zero, large-integer, and help-output behavior.
- Written work: seven worked solutions with derivations and arithmetic checks.
- Source caveat: the supplied book is *Cryptology - how to crack it*, Lars Ramkilde Knudsen, first edition (2018), printed page 23. Its equivalence to the course's *Cryptology in Essence* edition remains unconfirmed.
- No submission or instructor approval is implied.

## Exercise difficulty

| Exercise | Topic | Difficulty | Study estimate |
|---|---|---|---|
| 2.1 | Prescribed GCD and LCM | Easy | 5-10 min |
| 2.2 | Consequence of equal GCD and LCM | Medium | 10-15 min |
| 2.3 | Three primality questions | Easy | 5-10 min |
| 2.4 | Repunit compositeness | Medium | 10-15 min |
| 2.5 | Counterexample to a prime-product conjecture | Medium | 10-20 min |
| 2.6 | Two modular calculations | Easy | 5-10 min |
| 2.7 | Modular inverse via Euclid | Easy | 5-10 min |

Suggested order: 2.1, 2.3, 2.6, 2.7, then 2.2, 2.4, 2.5. Allow 50-90 minutes to work through the solutions, plus 15-20 minutes for final checks. These are study estimates, not elapsed implementation time.

## Verification

From the project root:

```bash
python3 -m unittest discover -s tests -v
python3 run_gcd.py 1071 462
```

Expected: nine passing tests and the GCD output `21`.

The [solution document](../exercises/week01-solutions.md) contains a reproducible standard-library arithmetic check. Successful execution prints `All arithmetic checks passed.` This numerical check supplements, rather than replaces, the general proofs.

The solutions were drafted with a Sol-low worker, reviewed with a Sol-high reviewer, and independently checked by the coordinating agent. Review found one difficulty-label inconsistency; it was corrected and re-reviewed. No mathematical findings remained open.

## Before class or submission

1. Confirm the seven questions match the assigned textbook edition.
2. Work through the derivations and explain why each answer holds.
3. Run the tests and the arithmetic check.
4. Explain the GCD loop: replacing `(a, b)` with `(b, a % b)` preserves the common divisors; when the second value becomes zero, the first is the GCD.
5. Follow the instructor's submission and academic-integrity requirements.

The original textbook and lecture PDFs are intentionally not included in this public repository.
