def gcd(a: int, b: int) -> int:
    """Return the non-negative greatest common divisor of two integers."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
