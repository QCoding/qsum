from qsum.core.checksum import checksum
from qsum.core.types import checksum_to_type
from qsum.tests.constants import BYTES_IN_CHECKSUM

# noinspection PyUnresolvedReferences
from qsum.tests.fixtures import *


def test_checksum_0():
    c = checksum(0)
    assert c == b"\x00\x00_\xec\xebf\xff\xc8o8\xd9Rxlmily\xc2\xdb\xc29\xddN\x91\xb4g)\xd7:'\xfbW\xe9", "Validate a specific checksum"


def test_integers_generate_unique_checksums(range_2_16):
    value_checksums = set(map(checksum, range_2_16))
    assert len(value_checksums) == len(range_2_16)


def test_integer_type():
    c = checksum(15)
    assert checksum_to_type(c) == int


def test_bytes_in_checksum():
    c = checksum(2043535)
    assert len(c) == BYTES_IN_CHECKSUM
