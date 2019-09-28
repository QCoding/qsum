# pylint: disable=redefined-outer-name
import pytest

from qsum import checksum, Checksum

CHECKSUM_CLASS_VALUE = -3453535


@pytest.fixture(scope='function')
def checksum_class():
    return Checksum(checksum(CHECKSUM_CLASS_VALUE))


def test_checksum_class_type(checksum_class):
    assert checksum_class.type == int


def test_checksum_class_checksum_bytes(checksum_class):
    assert checksum_class.checksum_bytes == checksum(CHECKSUM_CLASS_VALUE)


def test_checksum_class_checksum_hexdigest(checksum_class):
    assert checksum_class.hex() == '000063bd81fe542f91f3e2f53861e28fdb4ee8533e1c581cb98362f3190f8a6caff4'


def test_checksum_class_repr(checksum_class):
    assert repr(
        checksum_class) == "Checksum(000063bd81fe542f91f3e2f53861e28fdb4ee8533e1c581cb98362f3190f8a6caff4)"


def test_checksum_class_str(checksum_class):
    assert str(checksum_class) == "Checksum(int:63bd81fe542f91f3e2f53861e28fdb4ee8533e1c581cb98362f3190f8a6caff4)"


def test_checksum_class_eq(checksum_class):
    assert checksum_class == Checksum.checksum(CHECKSUM_CLASS_VALUE)
