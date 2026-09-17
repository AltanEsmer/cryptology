# Week 1 worked solutions

Start with one exercise. Read the calculation, cover the answer, and repeat the calculation yourself. The optional questions take about a minute each.

## Exercise 2.1: Find numbers with GCD 2 and LCM 30

The **GCD** is the largest number that divides both numbers. The **LCM** is the smallest positive number that both numbers divide.

We need $\gcd(a,b)=2$ and $\operatorname{lcm}(a,b)=30$.

1. Try $a=6$ and $b=10$.
2. List their divisors. For 6 they are $1,2,3,6$. For 10 they are $1,2,5,10$. The largest shared divisor is **2**.
3. List their positive multiples until they meet. For 6 they are $6,12,18,24,30$. For 10 they are $10,20,30$. The first shared multiple is **30**.

So **$a=6$, $b=10$ works**. Check the useful identity $\gcd(a,b)\operatorname{lcm}(a,b)=ab$ with $2\cdot30=6\cdot10=60$.

<details>
<summary>Want all the positive answers?</summary>

Since the GCD is 2, write $a=2x$ and $b=2y$, where $x$ and $y$ share no factor greater than 1. The identity above gives

$$4xy=60,\qquad xy=15.$$

The positive factor pairs of 15 are $(1,15)$ and $(3,5)$. Both have GCD 1. Multiply each entry by 2 to obtain $(2,30)$ and $(6,10)$. Swapping the entries also works.

</details>

Try it. Does $(4,15)$ work? Check its GCD first. Answer: no, its GCD is 1.

## Exercise 2.2: What if the GCD equals the LCM?

For positive numbers, the GCD cannot be larger than either number. The LCM cannot be smaller than either number.

For example, with 6 and 10, the GCD is 2 and the LCM is 30. Those values sit on opposite sides of both numbers.

1. Call the shared GCD and LCM $d$.
2. Because $d$ divides $a$, we have $d\le a$. Because $a$ divides $d$, we also have $a\le d$.
3. Together these give $d\le a\le d$, so $a=d$.
4. Apply the same steps to $b$. Then $b=d$ too.

Therefore **$a=b$**. This also works in reverse. If $a=b=8$, both the GCD and LCM are 8. The same holds for any positive value.

Try it. What are the GCD and LCM of 12 and 12? Answer: both are 12.

<details>
<summary>If zero or negative inputs are allowed</summary>

The main answer uses positive integers. With signed nonzero integers and nonnegative GCD and LCM, the conclusion is $|a|=|b|$. For example, 2 and $-2$ have GCD and LCM 2. Under the conventions $\gcd(0,0)=0$ and $\operatorname{lcm}(0,n)=0$, the pair $(0,0)$ works too. A pair with exactly one zero does not.

</details>

## Exercise 2.3: Which of these numbers are prime?

A prime is an integer greater than 1 whose only positive divisors are 1 and itself. One factor between those two is enough to prove that a number is composite.

### 1. Is 31 prime?

1. Only test primes up to $\sqrt{31}\approx5.57$. These are 2, 3, and 5.
2. Division by 2 leaves remainder 1, since $31=2\cdot15+1$.
3. Division by 3 leaves remainder 1, since $31=3\cdot10+1$.
4. Division by 5 leaves remainder 1, since $31=5\cdot6+1$.

None divides 31, so **31 is prime**.

Why stop at the square root? If $31=ab$ with both factors greater than 1, at least one factor must be at most $\sqrt{31}$. Otherwise $ab>31$. That smaller factor would have a prime divisor among 2, 3, and 5.

### 2. Is $13^{13}$ prime?

Write the power as a product:

$$13^{13}=13\cdot13^{12}.$$

Both factors exceed 1. Therefore **$13^{13}$ is composite**. No large calculation is needed.

### 3. Is $13^{13}+1$ prime?

1. 13 is odd. Multiplying odd numbers gives an odd number, so $13^{13}$ is odd.
2. Add 1 to get an even number greater than 2.
3. Therefore 2 is a nontrivial divisor.

So **$13^{13}+1$ is composite**. A numerical check is

$$302875106592254=2\cdot151437553296127.$$

Try it. Is $7^5+1$ prime? Answer: no, it is even and greater than 2.

## Exercise 2.4: Are these numbers made of ones prime?

Check a small divisor before trying to factor a large number completely.

1. Add the digits. For 111 the sum is 3, so 3 divides it. The same rule covers the numbers with 6, 9, or 12 ones.
2. For the remaining numbers, group the digits in pairs. For example, $1111=11\cdot101$. Every listed number with an even number of ones is divisible by 11.
3. Exhibit one factorization for each number.

| Number from the exercise | Factorization |
| --- | --- |
| 111 | $3\cdot37$ |
| 1,111 | $11\cdot101$ |
| 111,111 | $3\cdot37,037$ |
| 11,111,111 | $11\cdot1,010,101$ |
| 111,111,111 | $3\cdot37,037,037$ |
| 1,111,111,111 | $11\cdot101,010,101$ |
| 111,111,111,111 | $3\cdot37,037,037,037$ |

**None of the seven numbers is prime.** Every row expresses the number as two integers greater than 1. The factors do not need to be prime themselves.

Try it. Why is 111,111 divisible by both 3 and 11? Answer: its digit sum is 6, and $111111=11\cdot10101$.

## Exercise 2.5: Does multiplying the first primes and adding 1 always give a prime?

The first few attempts work:

$$2+1=3,\qquad2\cdot3+1=7,\qquad2\cdot3\cdot5+1=31.$$

But a few successful examples do not prove that the rule always works. One failed example disproves it.

1. Take the first six primes, $2,3,5,7,11,13$.
2. Multiply them in steps: $2\cdot3=6$, $6\cdot5=30$, $30\cdot7=210$, $210\cdot11=2310$, $2310\cdot13=30030$.
3. Add 1 to get 30031.
4. Factor the result: $30031=59\cdot509$.

So **no, the result is not always prime**. The counterexample uses $i=6$.

Check the multiplication with $59\cdot509=59\cdot500+59\cdot9=29500+531=30031$.

The construction does guarantee something useful. Dividing the product-plus-one by any prime in the original product leaves remainder 1. New prime factors can still divide it, as 59 and 509 do here.

Try it. What remainder does 30031 leave when divided by 13? Answer: 1, because $30030=13\cdot2310$.

## Exercise 2.6: Find remainders without huge powers

“Modulo $m$” means “keep the remainder after division by $m$.” You can replace bases by their remainders before calculating powers.

### 1. Find $(34^4+17^9)\bmod16$

1. $34=2\cdot16+2$, so replace 34 with 2.
2. $17=1\cdot16+1$, so replace 17 with 1.
3. Calculate $2^4+1^9=16+1=17$.
4. Divide 17 by 16. The remainder is **1**.

In symbols,

$$34^4+17^9\equiv2^4+1^9\equiv17\equiv1\pmod{16}.$$

### 2. Find $(701+55)^{98235411111}\bmod7$

1. Add the base: $701+55=756$.
2. Divide by 7: $756=7\cdot108$, so the remainder is 0.
3. A positive power of a multiple of 7 is still a multiple of 7.

The remainder is **0**. The enormous exponent does not change that answer.

Try it. Find $18^5\bmod17$. Answer: $18\equiv1\pmod{17}$, so the remainder is 1.

## Exercise 2.7: Find the inverse of 8 modulo 71

We want a number $x$ such that multiplying it by 8 leaves remainder 1 after division by 71. In symbols, $8x\equiv1\pmod{71}$.

1. Try 9. Then $8\cdot9=72$.
2. Since $72=71+1$, the remainder is 1.

Therefore **the inverse is 9**.

For larger numbers, use Euclid's algorithm to find the answer without guessing:

$$71=8\cdot8+7,$$
$$8=1\cdot7+1,$$
$$7=7\cdot1+0.$$

The last nonzero remainder is 1, so the GCD is 1 and an inverse exists. Work backward from the line containing 1:

$$1=8-7.$$

The first line says $7=71-8\cdot8$. Substitute it:

$$1=8-(71-8\cdot8)=9\cdot8-71.$$

The coefficient of 8 is 9, our inverse. Adding any multiple of 71 gives another representative of the same inverse, so all integer answers are $9+71k$.

Try it. Is 80 also an inverse? Answer: yes, $80=9+71$ and $8\cdot80=640=9\cdot71+1$.

## Run the week 1 GCD implementation

From the repository root, run:

```bash
python3 run_gcd.py 48 18
```

The output is `6`. Here is what the loop in [number_theory.py](../crypto_library/number_theory.py) does:

| Current pair $(a,b)$ | Division | Next pair $(b,a\bmod b)$ |
| --- | --- | --- |
| $(48,18)$ | $48=2\cdot18+12$ | $(18,12)$ |
| $(18,12)$ | $18=1\cdot12+6$ | $(12,6)$ |
| $(12,6)$ | $12=2\cdot6+0$ | $(6,0)$ |

Stop when the second value is zero. The first value, 6, is the GCD.

Why can we replace the pair? If a number divides both $a$ and $b$, it also divides the remainder $a-qb$. Conversely, a number dividing $b$ and that remainder divides $a=qb+r$. The common divisors stay the same, and the remainders get smaller until the loop stops. The implementation first takes absolute values so negative inputs work too. A zero input returns the absolute value of the other input, including 0 for `(0, 0)`.

Python's integers also support the course's 100-to-500-bit inputs. No extra number library is needed. Try large inputs with a known GCD:

```bash
python3 - <<'PY'
from crypto_library.number_theory import gcd

factor = 2**498 - 1
a, b = 2 * factor, 3 * factor
print(a.bit_length(), b.bit_length())
print(gcd(a, b) == factor)
PY
```

Expected output:

```text
499 500
True
```

The inputs are 499 and 500 bits long. The shared factor is the GCD because 2 and 3 share no divisor greater than 1. A bit is one binary digit, so bit length measures the size of the integer, not the number of decimal digits.

## Check the arithmetic yourself

Copy this block into a terminal at the repository root. It checks the numerical answers using only Python's standard library.

```bash
python3 - <<'PY'
import math

pairs = [(a, b) for a in range(1, 31) for b in range(a, 31)
         if math.gcd(a, b) == 2 and a * b // math.gcd(a, b) == 30]
assert pairs == [(2, 30), (6, 10)]
for a in range(1, 31):
    for b in range(1, 31):
        assert (math.gcd(a, b) == a * b // math.gcd(a, b)) == (a == b)
assert [d for d in range(1, 32) if 31 % d == 0] == [1, 31]
assert all(31 % p == 1 for p in (2, 3, 5))
assert 13**13 == 302875106592253
assert 13**13 % 13 == 0
assert 13**13 + 1 == 2 * 151437553296127
for n, d, q in [(111, 3, 37), (1111, 11, 101),
                (111111, 3, 37037), (11111111, 11, 1010101),
                (111111111, 3, 37037037),
                (1111111111, 11, 101010101),
                (111111111111, 3, 37037037037)]:
    assert n == d * q and 1 < d < n and 1 < q < n
assert math.prod([2, 3, 5, 7, 11, 13]) + 1 == 59 * 509 == 30031
assert (34**4 + 17**9) % 16 == 1
assert pow(701 + 55, 98235411111, 7) == 0
for a, q, b, r in [(71, 8, 8, 7), (8, 1, 7, 1), (7, 7, 1, 0)]:
    assert a == q * b + r and 0 <= r < b
assert 9 * 8 - 71 == 1 and (8 * 9) % 71 == 1
print('All arithmetic checks passed.')
PY
```

The finite check for Exercise 2.2 is a sanity check. The argument in that solution proves the result for every positive pair. Three-argument `pow(base, exponent, modulus)` finds a remainder without storing the enormous power.

## Source notes

These solutions use Lars Ramkilde Knudsen's *Cryptology - how to crack it*, first edition, 2018, Chapter 2, printed page 23. All seven exercises were visually checked against PDF page 13 of the supplied `cryptology_essence.pdf`. Exercise 2.3 asks about **31**, correcting the previous transcription of 3. Commas in Exercise 2.4 group decimal digits. Exercise 2.6 takes the remainder of the whole first sum.

The course calls its book *Cryptology in Essence*. Equivalence with that named edition remains unconfirmed. The solutions follow the supplied book's actual statements. Source PDFs remain outside this public repository.
