from collections.abc import Sequence


def gcd(a: int, b: int) -> int:
    """Return the non-negative greatest common divisor of two integers."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def modular_inverse(a: int, modulus: int) -> int:
    """Return a's inverse in [0, modulus), or raise ValueError if none exists."""
    if type(a) is not int or type(modulus) is not int:
        raise TypeError("a and modulus must be integers")
    if modulus <= 1:
        raise ValueError("modulus must be greater than 1")
    old_r, r = modulus, a % modulus
    old_s, s = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    if old_r != 1:
        raise ValueError("a and modulus must be coprime")
    return old_s % modulus


def euler_phi(n: int) -> int:
    """Count the integers from 1 through n that are coprime to positive n."""
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be positive")
    result, remaining, prime = n, n, 2
    # ponytail: trial division suits coursework; use faster factoring for huge n.
    while prime * prime <= remaining:
        if remaining % prime == 0:
            result -= result // prime
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        result -= result // remaining
    return result


def chinese_remainder(remainders: Sequence[int], moduli: Sequence[int]) -> int:
    """Solve nonempty congruences with pairwise coprime moduli greater than 1."""
    if len(remainders) != len(moduli) or not moduli:
        raise ValueError("remainders and moduli must have equal nonzero lengths")
    if any(type(value) is not int for value in (*remainders, *moduli)):
        raise TypeError("remainders and moduli must contain integers")
    product = 1
    for modulus in moduli:
        if modulus <= 1:
            raise ValueError("moduli must be greater than 1")
        if gcd(product, modulus) != 1:
            raise ValueError("moduli must be pairwise coprime")
        product *= modulus
    result = 0
    for remainder, modulus in zip(remainders, moduli):
        partial = product // modulus
        result += remainder * partial * modular_inverse(partial, modulus)
    return result % product
