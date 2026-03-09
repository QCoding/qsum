# pylint: disable=missing-function-docstring,missing-class-docstring,too-few-public-methods
import hashlib
from unittest import mock

import pytest

from qsum.core.constants import DEFAULT_HASH_ALGO
from qsum.core.exceptions import QSumInvalidDataTypeException, QSumInvalidChecksum, QSumInvalidBytesDataType
from qsum.data import data_checksum
from qsum.data.data_logic import data_digest_from_checksum, resolve_hash_algo, bytes_to_digest
from qsum.tests.helpers import STR_CHECKSUM_OBJS, Custom


def test_invalid_type():
    custom = Custom()
    with pytest.raises(QSumInvalidDataTypeException) as err:
        data_checksum(custom, type(custom), hash_algo=DEFAULT_HASH_ALGO)
    assert str(err.value) == "{} is not a recognized checksummable type".format(type(custom))


def test_data_checksum_key_error_mock():
    """Verify that a KeyError in TYPE_TO_BYTES_FUNCTION is caught and reraised as QSumInvalidDataTypeException"""
    with mock.patch.dict('qsum.data.data_logic.TYPE_TO_BYTES_FUNCTION', {}, clear=True):
        with pytest.raises(QSumInvalidDataTypeException) as err:
            data_checksum('abc', str, hash_algo=DEFAULT_HASH_ALGO)
        assert str(err.value) == "<class 'str'> is not a recognized checksummable type"


@pytest.mark.parametrize('checksum_obj', STR_CHECKSUM_OBJS)
def test_data_digest_from_checksum(checksum_obj):
    data_digest = data_digest_from_checksum(checksum_obj)
    if not isinstance(checksum_obj, str):
        data_digest = data_digest.hex()
    assert data_digest == 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'


def test_invalid_type_passed_to_data_digest_from_checksum():
    with pytest.raises(QSumInvalidChecksum):
        data_digest_from_checksum(123)


def test_consistent_hash_algo_resolution():
    assert resolve_hash_algo('sha256') == resolve_hash_algo(hashlib.sha256)


def test_bytes_to_digest_invalid_bytes_data():
    with pytest.raises(QSumInvalidBytesDataType):
        bytes_to_digest([1, 2, 3], hash_algo=DEFAULT_HASH_ALGO)
