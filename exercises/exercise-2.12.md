# Exercise 2.12 - Chinese Remainder Theorem

Source: Lars Ramkilde Knudsen, *Cryptology - how to crack it*, first edition (2018), printed page 24 (page 14 of the supplied `cryptology_essence.pdf`). Both parts were checked against the scanned page. This is a worked study solution.

## Setup and notation

Let $p$ and $q$ be distinct primes and $n=pq$. We use $\mathbb Z_n$ with representatives $0,1,\ldots,n-1$. The exercise asks us to prove the reconstruction formula below, then use it to solve a pair of congruences.

The notation $q^{-1}\bmod p$ means the **multiplicative inverse** of $q$ modulo $p$: an integer $u$ such that $qu\equiv1\pmod p$. It does not mean the ordinary fraction $1/q$. The inverses exist because distinct primes are coprime.

## Part 1: prove the reconstruction formula

For $x\in\mathbb Z_n$, define

$$
z=\big[(x\bmod p)q(q^{-1}\bmod p)
       +(x\bmod q)p(p^{-1}\bmod q)\big]\bmod n.
$$

We must show $z=x$.

**Step 1: reduce modulo $p$.** The second term contains a factor $p$, so it vanishes. In the first term, $q(q^{-1}\bmod p)\equiv1\pmod p$. Therefore

$$z\equiv(x\bmod p)\cdot1+0\equiv x\pmod p.$$

**Step 2: reduce modulo $q$.** The first term contains a factor $q$, so it vanishes. The inverse in the second term gives $p(p^{-1}\bmod q)\equiv1\pmod q$. Thus

$$z\equiv0+(x\bmod q)\cdot1\equiv x\pmod q.$$

Reducing the whole expression modulo $n$ does not change either of these congruences, since both $p$ and $q$ divide $n$.

**Step 3: combine the conclusions.** Both $p$ and $q$ divide $z-x$. Since $\gcd(p,q)=1$, their product divides $z-x$, so

$$z\equiv x\pmod{pq}.$$

Both $z$ and $x$ lie in $\{0,\ldots,pq-1\}$. Hence $|z-x|<pq$, and the only multiple of $pq$ in that range is zero. Therefore **$z=x$**.

This also explains uniqueness: any two solutions with the same remainders differ by a multiple of $pq$, so there is exactly one representative in $\mathbb Z_{pq}$.

### Why the formula works

Each coefficient preserves one remainder and contributes zero to the other:

| Coefficient | Modulo $p$ | Modulo $q$ |
|---|---|---|
| $q(q^{-1}\bmod p)$ | $1$ | $0$ |
| $p(p^{-1}\bmod q)$ | $0$ | $1$ |

Multiplying these coefficients by the desired remainders and adding reconstructs the number modulo $pq$.

## Part 2: solve the given congruences

Here $p=7$, $q=11$, and $n=77$. We want

$$x\equiv5\pmod7,\qquad x\equiv8\pmod{11}.$$

**Step 1: find the inverses.**

- $11\equiv4\pmod7$ and $4\cdot2=8\equiv1\pmod7$, so $11^{-1}\equiv2\pmod7$.
- $7\cdot8=56\equiv1\pmod{11}$, so $7^{-1}\equiv8\pmod{11}$.

**Step 2: substitute into the reconstruction formula.**

$$
x\equiv5\cdot11\cdot2+8\cdot7\cdot8
 =110+448=558\pmod{77}.
$$

**Step 3: reduce to the required range.** Since $558=7\cdot77+19$,

$$\boxed{x=19\text{ in }\mathbb Z_{77}.}$$

**Check:** $19=2\cdot7+5$ and $19=1\cdot11+8$, so both required remainders are correct. All integer solutions are $x=19+77k$ for $k\in\mathbb Z$.

### Alternative derivation by substitution

The first congruence says $x=5+7t$. Substituting into the second gives

$$5+7t\equiv8\pmod{11}\quad\Longrightarrow\quad7t\equiv3\pmod{11}.$$

Multiply by the inverse $8$ of $7$:

$$t\equiv24\equiv2\pmod{11}.$$

Thus $t=2+11k$ and $x=5+7(2+11k)=19+77k$, agreeing with the formula.

## Study reminders

- Pair each remainder with the **other modulus** and that modulus's inverse: the remainder modulo $p$ is multiplied by $q(q^{-1}\bmod p)$.
- Reduce the entire sum modulo $pq$ at the end. The intermediate value $558$ is congruent to the answer but is outside $\mathbb Z_{77}$'s chosen range.
- Congruence modulo both factors implies congruence modulo their product because the factors are coprime. The proof works for any two coprime positive moduli greater than 1, even if they are composite.

## Reproducible arithmetic check

Run this with Python 3.9 or newer. It checks every possible $x$ for the example moduli and independently enumerates the solutions to Part 2. The general proof is the argument above; this finite check verifies the example arithmetic.

```bash
python3 - <<'PY'
p, q = 7, 11
n = p * q
u, v = pow(q, -1, p), pow(p, -1, q)
assert (u, v) == (2, 8)
for x in range(n):
    z = ((x % p) * q * u + (x % q) * p * v) % n
    assert z == x
assert 5 * q * u + 8 * p * v == 558
assert 558 % n == 19
solutions = [x for x in range(n) if x % p == 5 and x % q == 8]
assert solutions == [19]
print('All 77 reconstructions passed; unique solution: x = 19.')
PY
```
