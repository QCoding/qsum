# pylint: disable=missing-function-docstring,missing-class-docstring,too-few-public-methods
import hashlib

import pytest

from qsum import checksum
from qsum.core.constants import DEFAULT_HASH_ALGO
from qsum.core.exceptions import QSumInvalidDataTypeException, QSumInvalidChecksum
from qsum.data import data_checksum
from qsum.data.data_logic import data_digest_from_checksum, resolve_hash_algo


class Custom:
    def __init__(self):
        pass


@pytest.mark.xfail(raises=QSumInvalidDataTypeException, strict=True)
def test_invalid_type():
    custom = Custom()
    _ = data_checksum(custom, type(custom), hash_algo=DEFAULT_HASH_ALGO)


def test_data_digest_from_checksum():
    assert data_digest_from_checksum(
        checksum('123')).hex() == 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'


@pytest.mark.xfail(raises=QSumInvalidChecksum)
def test_invalid_type_passed_to_data_digest_from_checksum():
    data_digest_from_checksum(123)


def test_consistent_hash_algo_resolution():
    assert resolve_hash_algo('sha256') == resolve_hash_algo(hashlib.sha256)
