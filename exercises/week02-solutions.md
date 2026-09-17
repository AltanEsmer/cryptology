# Week 2 solutions, one calculation at a time

These solutions cover Exercises 2.8–2.12, including Wednesday's proof in 2.12(1).
The Week 2 sheet also checks 2.6 and 2.7, which are in [Week 1](week01-solutions.md).

Source checked against the supplied *Cryptology - how to crack it* (2018), printed pages 23–24, PDF pages 13–14. The course sheet calls the book *Cryptology - in essence*. The edition match is unverified, so the numbers and exercise statements below follow the supplied PDF.

Try one numbered part at a time. Cover the answer, do one line, then compare.

## The notation you need

- `a mod n` is the remainder after division by `n`.
- `a ≡ b (mod n)` means that `a` and `b` have the same remainder.
- `gcd(a, b)` is the largest positive integer dividing both numbers.
- An inverse of `a` modulo `n` is a number `z` with `a·z ≡ 1 (mod n)`.
- `φ(n)` counts the integers from 1 to `n` that are coprime to `n`. Coprime means their gcd is 1.
- `Z_n` uses representatives `0, 1, …, n−1`.

## Exercise 2.8. Gcd, coefficients, and an inverse

The numbers are `a = 357` and `b = 1234`.

### Part 1. Find gcd(357, 1234)

Divide, keep the remainder, and repeat with the last two numbers.

```text
1234 = 3·357 + 163
 357 = 2·163 + 31
 163 = 5·31  + 8
  31 = 3·8   + 7
   8 = 1·7   + 1
   7 = 7·1   + 0
```

The last nonzero remainder is **1**, so `gcd(357, 1234) = 1`.

Why this works follows from the first line. Any divisor of both 1234 and 357 also divides `1234 − 3·357 = 163`. You keep the common divisors while shrinking the numbers.

### Part 2. Find s and t with 357s + 1234t = 1

Work upward from the remainder 1. Replace each remainder using the previous division.

```text
1 = 8 − 7
  = 8 − (31 − 3·8)
  = 4·8 − 31
  = 4·(163 − 5·31) − 31
  = 4·163 − 21·31
  = 4·163 − 21·(357 − 2·163)
  = 46·163 − 21·357
  = 46·(1234 − 3·357) − 21·357
  = 46·1234 − 159·357
```

Thus **s = −159 and t = 46**.

Check the actual arithmetic.

```text
357·(−159) + 1234·46 = −56763 + 56764 = 1
```

### Part 3. Find z with 357z ≡ 1 (mod 1234)

Use the equation you just found.

```text
357·(−159) + 1234·46 = 1
```

Modulo 1234, the term `1234·46` becomes zero. This leaves `357·(−159) ≡ 1`.
Turn the negative answer into the representative between 0 and 1233.

```text
z = −159 + 1234 = 1075
```

**Answer. z = 1075.** Check `357·1075 = 383775 = 311·1234 + 1`.

Pause and try it. Why does adding 1234 to an inverse preserve the answer? Because the product changes by a multiple of 1234.

## Exercise 2.9. Find numbers with a given phi value

Two useful facts reduce the trial and error.

- If `p` is prime, `φ(p) = p−1`. Every number from 1 to `p−1` is coprime to `p`.
- If `a` and `b` are coprime, `φ(ab) = φ(a)φ(b)`.

### Part 1. Find x with φ(x) = 4

Try a prime with `p−1 = 4`. This gives `p = 5`.
The numbers `1, 2, 3, 4` are all coprime to 5.

**One answer is x = 5.** The question asks for a value, so one verified example is enough.

### Part 2. Find x with φ(x) = 300

Trying `x = 301` as a prime does not work. It equals `7·43`.
Instead, split 300 into factors that are one less than primes.

```text
300 = 10·30 = (11−1)(31−1)
```

Both 11 and 31 are prime, and they are distinct. Choose `x = 11·31 = 341`.

**Answer. φ(341) = φ(11)φ(31) = 10·30 = 300.**

### Part 3. Find more than one x with φ(x) = 10

First choose the prime `11`, since `11−1 = 10`.
Then multiply 11 by 2. The factors are coprime, and `φ(2) = 1`.

```text
φ(11) = 10
φ(22) = φ(2)φ(11) = 1·10 = 10
```

**Two answers are x = 11 and x = 22.**
For a direct check, the ten residues coprime to 22 are `1, 3, 5, 7, 9, 13, 15, 17, 19, 21`.

## Exercise 2.10. Compute phi values

### Part 1. a = 491401 and b = 701

First notice `491401 = 701²`.
We need to know that 701 is prime before using the prime-power formula.

Since `26² < 701 < 27²`, a composite 701 would have a prime divisor at most 26.
Check those primes.

```text
prime          2  3  5  7  11  13  17  19  23
701 remainder  1  2  1  1   8  12   4  17  11
```

None divides 701. Therefore 701 is prime.

For `701²`, the numbers that fail to be coprime are precisely the multiples of 701. There are 701 of them from 1 to `701²`.

```text
φ(491401) = φ(701²) = 701² − 701 = 490700
φ(701) = 701 − 1 = 700
```

**Answers. φ(a) = 490700 and φ(b) = 700.**

### Part 2. φ(9), φ(12), and φ(12·9)

Start with the small cases by counting.

```text
Coprime to 9:   1, 2, 4, 5, 7, 8     so φ(9) = 6
Coprime to 12:  1, 5, 7, 11           so φ(12) = 4
```

For the product, factor `108 = 2²·3³`. Remove the multiples of each distinct prime using the phi formula.

```text
φ(108) = 108·(1−1/2)·(1−1/3)
       = 108·(1/2)·(2/3)
       = 36
```

**Answers. 6, 4, and 36.**

The tempting calculation `φ(12)φ(9) = 24` is wrong for `φ(108)` because `gcd(12, 9) = 3`. The product rule requires coprime factors.

## Exercise 2.11. Combine two remainders

Find `0 ≤ x < 143` with `x ≡ 3 (mod 11)` and `x ≡ 5 (mod 13)`.

1. Write every number satisfying the first condition as `x = 3 + 11k`.
2. Substitute into the second condition.

   ```text
   3 + 11k ≡ 5 (mod 13)
       11k ≡ 2 (mod 13)
   ```

3. Since `11 ≡ −2 (mod 13)`, this becomes `−2k ≡ 2`. Multiply by the inverse of −2, which is 6 modulo 13.

   ```text
   k ≡ 12 (mod 13)
   ```

4. Choose `k = 12`, giving `x = 3 + 11·12 = 135`.

**Answer. x = 135.**

Check `135 = 12·11 + 3` and `135 = 10·13 + 5`.
Since 11 and 13 are coprime, CRT says this is the only answer in `0 ≤ x < 143`.

## Exercise 2.12. Why the CRT formula works

### Part 1. Wednesday's proof

Let `p` and `q` be different primes, let `n = pq`, and take `x` in `Z_n`.
Write the proposed construction with shorter names.

```text
r = x mod p         u = inverse of q modulo p
s = x mod q         v = inverse of p modulo q

z = (r·q·u + s·p·v) mod n
```

The inverses exist because different primes are coprime. The two products have deliberately chosen remainders.

**Step 1. Reduce modulo p.**

The term `s·p·v` has a factor `p`, so it becomes zero. The inverse gives `q·u ≡ 1 (mod p)`.

```text
z ≡ r·1 + 0 ≡ r ≡ x (mod p)
```

Reducing modulo `n` first does not affect this result, since subtracting a multiple of `pq` also subtracts a multiple of `p`.

**Step 2. Reduce modulo q.**

Now `r·q·u` becomes zero, while `p·v ≡ 1 (mod q)`.

```text
z ≡ 0 + s·1 ≡ s ≡ x (mod q)
```

**Step 3. Turn the matching remainders into equality.**

Both `p` and `q` divide `z−x`. Since they are coprime, their product `pq` divides `z−x`.
But `x` and `z` both lie between 0 and `pq−1`. Their difference is strictly between `−pq` and `pq`.
The only multiple of `pq` in that interval is zero.

Therefore **z = x**.

The useful idea is that `q·u` has remainder 1 modulo `p` and 0 modulo `q`. The other product does the reverse. Each term supplies exactly one of the required remainders.

### Part 2. x ≡ 5 (mod 7) and x ≡ 8 (mod 11)

Here `p = 7`, `q = 11`, and `n = 77`.

1. Find the inverse of 11 modulo 7. Since `11·2 = 22 ≡ 1 (mod 7)`, use `u = 2`.
2. Find the inverse of 7 modulo 11. Since `7·8 = 56 ≡ 1 (mod 11)`, use `v = 8`.
3. Substitute the remainders and inverses into the formula.

   ```text
   x = (5·11·2 + 8·7·8) mod 77
     = (110 + 448) mod 77
     = 558 mod 77
     = 19
   ```

**Answer. x = 19 in Z_77.**
Check `19 = 2·7 + 5` and `19 = 1·11 + 8`.

## Run the implementations

The functions live in [number_theory.py](../crypto_library/number_theory.py).
Run this from the repository root.

```bash
python3 - <<'PY'
from crypto_library.number_theory import modular_inverse, euler_phi, chinese_remainder

print(modular_inverse(357, 1234))
print(euler_phi(491401))
print(chinese_remainder([5, 8], [7, 11]))
PY
```

Expected output is `1075`, `490700`, and `19`, on separate lines.

`modular_inverse` tracks coefficients during Euclid's divisions. It returns the inverse between 0 and `modulus−1`.
`euler_phi` factors the input by trial division, then subtracts one prime fraction for each distinct prime factor.
`chinese_remainder` applies the same construction as 2.12 to any nonempty sequence of pairwise coprime moduli.

Inputs must be integers, excluding booleans. Inverse and CRT moduli must exceed 1. Phi accepts `n ≥ 1`, with `φ(1) = 1`.
CRT requires equally long remainder and modulus sequences. Invalid types raise `TypeError`; invalid mathematical inputs raise `ValueError`.

Trial division is suitable for these exercise numbers. Factoring cryptographic-size integers requires a different approach.
For an inverse outside this implementation exercise, Python already provides `pow(a, -1, modulus)`.

Run the checks.

```bash
python3 -m unittest discover -s tests -p 'test_number_theory.py' -v
```
