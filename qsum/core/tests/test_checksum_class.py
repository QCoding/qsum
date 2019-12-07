# pylint: disable=redefined-outer-name,missing-function-docstring
import functools

import pytest

from qsum import checksum, Checksum
from qsum.core.constants import ChecksumCollection
from qsum.core.exceptions import QSumInvalidChecksum
from qsum.data.data_logic import data_digest_from_checksum
from qsum.types.type_logic import checksum_to_type

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
        checksum_class) == "Checksum('{}',is_checksum=True)".format(EXPECTED_CHECKSUM)


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
    checksum_is_checksum = functools.partial(Checksum, is_checksum=True)

    # three types of checksum objects supported
    checksums = list(
        map(checksum_is_checksum,
            (Checksum('foo'), '00012c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae',
             b'\x00\x01,&\xb4kh\xff\xc6\x8f\xf9\x9bE<\x1d0A4\x13B-pd\x83\xbf\xa0\xf9\x8a^\x88bf\xe7\xae')))

    assert checksums[0].checksum_bytes == checksums[1].checksum_bytes == checksums[2].checksum_bytes


def test_checksum_class_repr_eval(checksum_class):
    checksum_repr = repr(checksum_class)
    assert checksum_class.checksum_bytes == eval(checksum_repr).checksum_bytes  # pylint: disable=eval-used


@pytest.mark.xfail(raises=QSumInvalidChecksum, strict=True)
def test_checksum_non_checksum_like_object():
    Checksum(1, is_checksum=True)


def test_checksum_add():
    checksum_collection = Checksum(1) + Checksum(2)
    assert checksum_collection.hex() == 'ff1112e56c5e7ba9ec2ddd13fc983287f720eb103312bf3536480af0f7dfef255a12'
    assert checksum_to_type(checksum_collection.checksum_bytes) == ChecksumCollection


def test_checksum_add_order_dependent():
    assert Checksum(1) + Checksum(2) + Checksum(3) != Checksum(3) + Checksum(2) + Checksum(1)
