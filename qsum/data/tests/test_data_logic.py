# pylint: disable=missing-function-docstring,missing-class-docstring,too-few-public-methods
import hashlib

import pytest

from qsum.core.constants import DEFAULT_HASH_ALGO
from qsum.core.exceptions import QSumInvalidDataTypeException, QSumInvalidChecksum, QSumInvalidBytesDataType
from qsum.data import data_checksum
from qsum.data.data_logic import data_digest_from_checksum, resolve_hash_algo, bytes_to_digest
from qsum.tests.helpers import STR_CHECKSUM_OBJS, Custom


@pytest.mark.xfail(raises=QSumInvalidDataTypeException, strict=True)
def test_invalid_type():
    custom = Custom()
    _ = data_checksum(custom, type(custom), hash_algo=DEFAULT_HASH_ALGO)


@pytest.mark.parametrize('checksum_obj', STR_CHECKSUM_OBJS)
def test_data_digest_from_checksum(checksum_obj):
    data_digest = data_digest_from_checksum(checksum_obj)
    if not isinstance(checksum_obj, str):
        data_digest = data_digest.hex()
    assert data_digest == 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'


@pytest.mark.xfail(raises=QSumInvalidChecksum, strict=True)
def test_invalid_type_passed_to_data_digest_from_checksum():
    data_digest_from_checksum(123)


def test_consistent_hash_algo_resolution():
    assert resolve_hash_algo('sha256') == resolve_hash_algo(hashlib.sha256)


@pytest.mark.xfail(raises=QSumInvalidDataTypeException, strict=True)
def test_resolve_hash_algo_invalid():
    resolve_hash_algo('invalid_algo')


def test_resolve_hash_algo_fallback():
    # find an algorithm that is in available but not in hashlib
    available_not_in_hashlib = list(hashlib.algorithms_available - set(dir(hashlib)))
    if available_not_in_hashlib:
        algo_name = available_not_in_hashlib[0]
        algo = resolve_hash_algo(algo_name)
        # check that the algo name matches the requested one (ignoring case and dashes)
        assert algo().name.replace('-', '').lower() == algo_name.replace('-', '').lower()


@pytest.mark.xfail(raises=QSumInvalidBytesDataType)
def test_bytes_to_digest_invalid_bytes_data():
    bytes_to_digest([1, 2, 3], hash_algo=DEFAULT_HASH_ALGO)
