from qsum.core.checksum import checksum
from qsum.core.types import checksum_to_type

BYTES_IN_CHECKSUM = 34


def test_checksum_0():
    c = checksum(0)
    assert c == b"\x00\x00_\xec\xebf\xff\xc8o8\xd9Rxlmily\xc2\xdb\xc29\xddN\x91\xb4g)\xd7:'\xfbW\xe9", "Validate a specific checksum"


def test_integers_generate_unique_checksums():
    values = range(-2 ** 16, 2 ** 16)
    value_checksums = set(map(checksum, values))
    assert len(value_checksums) == len(values)


def test_integer_type():
    c = checksum(15)
    assert checksum_to_type(c) == int


def test_bytes_in_checksum():
    c = checksum(2043535)
    assert len(c) == BYTES_IN_CHECKSUM
