# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
import pytest

from qsum import Checksum
from qsum.core.exceptions import QSumInvalidTypeException, QSumInvalidPrefixException, QSumInvalidChecksum
from qsum.tests.helpers import INT_CHECKSUM_OBJS, Custom
from qsum.types.type_logic import prefix_to_type, checksum_to_type, type_to_prefix
from qsum.types.type_map import RESERVED_INVALID_PREFIX, UNREGISTERED_TYPE_PREFIX


def test_prefix_to_type():
    with pytest.raises(QSumInvalidPrefixException):
        prefix_to_type(RESERVED_INVALID_PREFIX)


@pytest.mark.parametrize('checksum_obj', INT_CHECKSUM_OBJS)
def test_checksum_to_type(checksum_obj):
    assert checksum_to_type(checksum_obj) == int


def test_checksum_to_type_invalid_type():
    with pytest.raises(QSumInvalidChecksum):
        checksum_to_type(Custom)


def test_type_to_prefix_custom_registered():
    assert type_to_prefix(Custom, allow_unregistered=True) == UNREGISTERED_TYPE_PREFIX


def test_type_to_prefix_custom_unregistered():
    with pytest.raises(QSumInvalidTypeException):
        type_to_prefix(Custom, allow_unregistered=False)


def test_expected_custom_type():
    with pytest.raises(QSumInvalidTypeException):
        _ = Checksum.checksum(Custom()).type
