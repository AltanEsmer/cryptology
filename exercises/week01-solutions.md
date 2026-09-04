# Week 1 - Chapter 2 Exercises

Source: the user-supplied `cryptology_essence.pdf`, whose title is *Cryptology - how to crack it*, Lars Ramkilde Knudsen, first edition (2018). The seven statements below were visually checked against PDF page 13, printed page 23. Mathematical notation is transcribed in Markdown/LaTeX; commas in Exercise 2.4 are digit-group separators.

**Edition caveat:** These are solutions to the supplied book. Its equivalence to the course's named *Cryptology in Essence* edition has not been confirmed; the exercise-number match alone does not establish course-edition equivalence.

Difficulty/time entries are estimated solving effort, not elapsed time. Verification commands use Python's standard library and should be run from the repository root.

## Exercise 2.1

**Problem:** Find values of $a$ and $b$ for which $\gcd(a,b)=2$ and $\operatorname{lcm}(a,b)=30$?

**Difficulty/time:** Easy, 5–10 minutes.

**Work:** Choose $a=6$ and $b=10$. Their prime factorizations are $6=2\cdot3$ and $10=2\cdot5$. Their only shared prime factor is 2, and the least common multiple contains each prime factor once: $2\cdot3\cdot5=30$.

More generally, for positive integers write $a=2x$, $b=2y$, where $\gcd(x,y)=1$. Since $\gcd(a,b)\operatorname{lcm}(a,b)=ab$, we get $60=4xy$, so $xy=15$. The coprime unordered factor pairs are $(1,15)$ and $(3,5)$.

**Answer:** One solution is $(a,b)=(6,10)$. All positive solutions, up to exchanging $a$ and $b$, are $(2,30)$ and $(6,10)$.

**Verification:** `python3 run_gcd.py 6 10` prints `2`. Independently, $6\cdot10/2=30$, verifying the LCM. Enumerating positive pairs with $a\le b\le30$ using `math.gcd` and `a*b//math.gcd(a,b)` gives exactly `[(2, 30), (6, 10)]`.

## Exercise 2.2

**Problem:** Assume that $\gcd(a,b)=\operatorname{lcm}(a,b)$. What can be said about $a$ and $b$?

**Difficulty/time:** Medium, 10–15 minutes.

**Work:** Under the positive-integer convention, let the common value be $d$. Because $d=\gcd(a,b)$ divides both positive integers, $d\le a$ and $d\le b$. Because $d=\operatorname{lcm}(a,b)$ is a positive multiple of each, $a\le d$ and $b\le d$. Thus $a=d=b$.

**Answer:** For positive integers, $a=b$; conversely, every positive pair with $a=b$ satisfies the equality. If signed, nonzero integers are allowed with nonnegative GCD and LCM, the conclusion is $|a|=|b|$, not necessarily $a=b$. With the convention $\operatorname{lcm}(0,n)=0$ and $\gcd(0,0)=0$, the pair $(0,0)$ also satisfies it, but a pair with exactly one zero does not.

**Verification:** Conversely, if $a=b=c>0$, both the GCD and LCM equal $c$, proving sufficiency as well as necessity. For the signed caveat, $a=2,b=-2$ gives GCD = LCM = 2 although $a\ne b$.

## Exercise 2.3

**Problem:** Assume $p$ is an integer greater than 1, and assume that none of the primes less than $p$ divides $p$. Then $p$ itself is a prime.

1. Is 3 a prime?
2. Is $13^{13}$ a prime?
3. Is $13^{13}+1$ a prime?

**Difficulty/time:** Easy, 5–10 minutes.

**Work:**

1. The only prime smaller than 3 is 2, which does not divide 3. Hence 3 is prime.
2. $13^{13}=13\cdot13^{12}$, a product of two integers greater than 1, so it is composite.
3. An odd number to a positive integer power is odd. Thus $13^{13}+1$ is even and greater than 2, so it is composite.

**Answer:** Respectively: yes, no, no.

**Verification:** The positive divisors of 3 are exactly 1 and 3. Numerically, $13^{13}=302875106592253$, which is divisible by 13, and $13^{13}+1=302875106592254=2\cdot151437553296127$. These explicit nontrivial factors check the two composite claims.

## Exercise 2.4

**Problem:** Which of the following integers (decimal notation) are primes?

111; 1,111; 111,111; 11,111,111; 111,111,111; 1,111,111,111; 111,111,111,111.

**Difficulty/time:** Medium, 10–15 minutes.

**Work:** A decimal integer is divisible by 3 when its digit sum is divisible by 3, because $10\equiv1\pmod3$. This covers repunits of lengths 3, 6, 9, and 12. For each remaining length (4, 8, 10), the length is even: since $10\equiv-1\pmod{11}$, the alternating sum of the digits is zero, giving divisibility by 11. Each number is greater than its exhibited divisor.

**Answer:** None of the seven integers is prime.

**Verification:** Explicit factorizations provide a direct check of every entry; the cofactors need not themselves be prime.

| Integer | Nontrivial factorization |
|---|---|
| 111 | $3\cdot37$ |
| 1,111 | $11\cdot101$ |
| 111,111 | $3\cdot37,037$ |
| 11,111,111 | $11\cdot1,010,101$ |
| 111,111,111 | $3\cdot37,037,037$ |
| 1,111,111,111 | $11\cdot101,010,101$ |
| 111,111,111,111 | $3\cdot37,037,037,037$ |

## Exercise 2.5

**Problem:** Let $p_1,p_2,p_3,\ldots$ be the list of primes in ascending order, that is, $p_1=2,p_2=3,p_3=5$ etc.

1. Is $p_1\cdot p_2\cdot\ldots\cdot p_{i-1}\cdot p_i+1$ a prime for all values of $i$? If yes, argue why this is the case. If no, show a counter example.

**Difficulty/time:** Medium, 10–20 minutes.

**Work:** Take $i=6$, so the first six primes are $2,3,5,7,11,13$. Then

$$2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30030+1=30031=59\cdot509.$$

Both factors exceed 1, so the result is composite. The construction guarantees only that none of the first $i$ primes divides the result: division by any of them leaves remainder 1. It does not exclude products of larger primes.

**Answer:** No. The counterexample $i=6$ gives $30031=59\cdot509$.

**Verification:** Direct multiplication yields $59\cdot509=59(500+9)=29500+531=30031$. Also $30031-1=30030$ is exactly the product of the first six primes.

## Exercise 2.6

**Problem:**

1. Find $34^4+17^9\bmod16$.
2. Find $(701+55)^{98235411111}\bmod7$.

**Difficulty/time:** Easy, 5–10 minutes.

**Work:** Interpret the first expression as the residue of the whole sum.

1. Reduce the bases: $34\equiv2\pmod{16}$ and $17\equiv1\pmod{16}$. Therefore $34^4+17^9\equiv2^4+1^9=17\equiv1\pmod{16}$.
2. $701+55=756=7\cdot108\equiv0\pmod7$. The exponent $98235411111$ is positive, so raising this multiple of 7 to that power still gives a multiple of 7.

**Answer:** The least nonnegative residues are (1) 1 and (2) 0.

**Verification:** `python3 -c 'print((34**4 + 17**9) % 16); print(pow(701 + 55, 98235411111, 7))'` prints `1` followed by `0`. Three-argument `pow` computes the second residue without constructing the enormous integer power.

## Exercise 2.7

**Problem:** Find the multiplicative inverse of 8 modulo 71.

**Difficulty/time:** Easy, 5–10 minutes.

**Work:** Apply Euclid's algorithm:

$$71=8\cdot8+7,\qquad8=1\cdot7+1,\qquad7=7\cdot1+0.$$

Thus $\gcd(8,71)=1$, so an inverse exists. Back-substitution gives

$$1=8-7=8-(71-8\cdot8)=9\cdot8-71.$$

Reducing modulo 71 gives $9\cdot8\equiv1\pmod{71}$.

**Answer:** $8^{-1}\equiv9\pmod{71}$. The least nonnegative representative is 9; all integer representatives are $9+71k$ for $k\in\mathbb Z$.

**Verification:** $8\cdot9=72=71+1$, so the remainder is 1. Each Euclidean line also has a valid remainder: $0\le7<8$, $0\le1<7$, and $0\le0<1$.

The following reproducible standard-library check covers the numerical claims across all seven exercises (successful execution prints `All arithmetic checks passed.`):

```bash
python3 - <<'PY'
import math

pairs = [(a, b) for a in range(1, 31) for b in range(a, 31)
         if math.gcd(a, b) == 2 and a * b // math.gcd(a, b) == 30]
assert pairs == [(2, 30), (6, 10)]
for a in range(1, 31):
    for b in range(1, 31):
        assert (math.gcd(a, b) == a * b // math.gcd(a, b)) == (a == b)
assert [d for d in range(1, 4) if 3 % d == 0] == [1, 3]
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
    assert a == q * b + r and 0 <= r < abs(b)
assert 8 % 1 == 0 and 71 % 1 == 0
assert 9 * 8 - 71 == 1 and (8 * 9) % 71 == 1
print('All arithmetic checks passed.')
PY
```

The finite check for Exercise 2.2 is a sanity check only; its general proof is the divisibility argument above.
