from qsum.core.checksum import checksum
from qsum.core.types import checksum_to_type


def test_basic_int_checksum():
    c = checksum(0)
    assert c == b"\x00\x00_\xec\xebf\xff\xc8o8\xd9Rxlmily\xc2\xdb\xc29\xddN\x91\xb4g)\xd7:'\xfbW\xe9", "Validate a specific checksum"
    assert len(c) == 34, "Validate the number of bytes of the checksum"
    assert checksum_to_type(c) == int
    assert c != checksum(1)
