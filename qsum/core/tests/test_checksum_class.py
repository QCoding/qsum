# pylint: disable=redefined-outer-name,missing-function-docstring
import functools

import pytest

from qsum import checksum, Checksum
from qsum.data.data_logic import data_digest_from_checksum

CHECKSUM_CLASS_VALUE = -3453535
EXPECTED_CHECKSUM = '000063bd81fe542f91f3e2f53861e28fdb4ee8533e1c581cb98362f3190f8a6caff4'


@pytest.fixture(scope='session')
def checksum_class():
    return Checksum(CHECKSUM_CLASS_VALUE)


def test_checksum_class_type(checksum_class):
    assert checksum_class.type == int


def test_checksum_class_checksum_bytes(checksum_class):
    assert checksum_class.checksum_bytes == checksum(CHECKSUM_CLASS_VALUE)


def test_checksum_class_checksum_hexdigest(checksum_class):
    assert checksum_class.hex() == EXPECTED_CHECKSUM


def test_checksum_class_repr(checksum_class):
    assert repr(
        checksum_class) == "Checksum({})".format(EXPECTED_CHECKSUM)


def test_checksum_class_str(checksum_class):
    assert str(checksum_class) == "Checksum(int:{})".format(data_digest_from_checksum(EXPECTED_CHECKSUM))


def test_checksum_class_eq(checksum_class):
    assert checksum_class == Checksum.checksum(CHECKSUM_CLASS_VALUE)


def test_from_checksum():
    assert Checksum.from_checksum(checksum(CHECKSUM_CLASS_VALUE)) == EXPECTED_CHECKSUM


def test_checksum_eq(checksum_class):
    assert checksum_class == Checksum(CHECKSUM_CLASS_VALUE)
    assert Checksum(CHECKSUM_CLASS_VALUE).hex() == checksum_class
    assert Checksum(CHECKSUM_CLASS_VALUE).checksum_bytes == checksum_class


def test_checksum_not_eq(checksum_class):
    assert Checksum(CHECKSUM_CLASS_VALUE + 1).hex() != checksum_class


def test_checksum_class_init():
    Checksum_is_checksum = functools.partial(Checksum, is_checksum=True)

    # three types of checksum objects supported
    checksums = list(
        map(Checksum_is_checksum,
            (Checksum('foo'), '00012c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae',
             b'\x00\x01,&\xb4kh\xff\xc6\x8f\xf9\x9bE<\x1d0A4\x13B-pd\x83\xbf\xa0\xf9\x8a^\x88bf\xe7\xae')))

    assert checksums[0].checksum_bytes == checksums[1].checksum_bytes == checksums[2].checksum_bytes


def test_checksum_class_repr(checksum_class):
    checksum_repr = repr(checksum_class)
    assert checksum_class.checksum_bytes == eval(checksum_repr).checksum_bytes
