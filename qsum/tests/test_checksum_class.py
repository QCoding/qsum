from qsum import checksum, Checksum


def test_checksum_class_type():
    csum = Checksum(checksum(-3453535))
    assert csum.type == int
