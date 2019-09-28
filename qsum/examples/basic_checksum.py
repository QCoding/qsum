from qsum import checksum


def main():
    """Compute the checksum of a string and print it's hex"""
    print(checksum('abcd').hex())


if __name__ == "__main__":
    main()
