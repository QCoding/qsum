from qsum import checksum


def main():
    """Example of using checksums to determine if the contents of a dict have changed """
    sub_dict = {1: 42, 2: 82}
    big_dict = {
        'a': sub_dict,
        'b': (6, 7, 8),
        'c': ['a', 'b', 'c'],
    }

    c_1 = checksum(big_dict)
    sub_dict[1] += 1
    c_2 = checksum(big_dict)

    # changing the contents of the dict changes the checksum
    assert c_1 != c_2

    sub_dict[1] -= 1
    c_3 = checksum(big_dict)

    # changing the contents back restores the original checksum
    assert c_1 == c_3


if __name__ == "__main__":
    main()
