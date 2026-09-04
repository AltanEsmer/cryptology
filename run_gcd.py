import argparse

from crypto_library.number_theory import gcd


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute gcd(a, b) with Euclid's algorithm."
    )
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    arguments = parser.parse_args()
    print(gcd(arguments.a, arguments.b))


if __name__ == "__main__":
    main()
