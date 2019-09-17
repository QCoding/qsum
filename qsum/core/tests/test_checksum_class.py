import pytest

from qsum import checksum, Checksum


@pytest.fixture(scope='function')
def checksum_class():
    return Checksum(checksum(-3453535))


def test_checksum_class_type(checksum_class):
    assert checksum_class.type == int


def test_checksum_class_checksum_bytes(checksum_class):
    assert checksum_class.checksum_bytes == checksum(-3453535)


def test_checksum_class_checksum_hexdigest(checksum_class):
    assert checksum_class.hexdigest() == '000063bd81fe542f91f3e2f53861e28fdb4ee8533e1c581cb98362f3190f8a6caff4'


def test_checksum_class_repr(checksum_class):
    assert repr(
        checksum_class) == "Checksum(000063bd81fe542f91f3e2f53861e28fdb4ee8533e1c581cb98362f3190f8a6caff4)"


def test_checksum_class_str(checksum_class):
    assert str(checksum_class) == "Checksum(int:63bd81fe542f91f3e2f53861e28fdb4ee8533e1c581cb98362f3190f8a6caff4)"
