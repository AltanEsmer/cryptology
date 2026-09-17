import argparse

from crypto_library.aes import encrypt_block


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Encrypt one 16-byte block with educational AES-128."
    )
    parser.add_argument("plaintext", help="16-byte plaintext as 32 hexadecimal digits")
    parser.add_argument("key", help="16-byte key as 32 hexadecimal digits")
    parser.add_argument("--rounds", type=int, choices=range(2, 11), default=10,
                        help="rounds (default: 10; fewer rounds are nonstandard)")
    arguments = parser.parse_args()
    inputs = []
    for name in ("plaintext", "key"):
        try:
            inputs.append(bytes.fromhex(getattr(arguments, name)))
        except ValueError:
            parser.error(f"{name} must contain hexadecimal byte pairs")
    try:
        ciphertext = encrypt_block(*inputs, rounds=arguments.rounds)
    except ValueError as error:
        parser.error(str(error))
    print(ciphertext.hex())


if __name__ == "__main__":
    main()
