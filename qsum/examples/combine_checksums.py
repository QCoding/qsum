from qsum import Checksum


def main():
    """Checksums can be combined"""
    object_1 = {'a': [1, 2, 3]}
    object_2 = {'b': [4, 5, 6]}

    c_1 = Checksum(object_1)
    c_2 = Checksum(object_2)

    combined = c_1 + c_2

    print(combined)


if __name__ == "__main__":
    main()
