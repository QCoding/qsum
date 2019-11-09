# pylint: disable=missing-function-docstring,missing-class-docstring,too-few-public-methods
import hashlib

import pytest

from qsum import Checksum
from qsum.core.constants import DEFAULT_HASH_ALGO
from qsum.core.exceptions import QSumInvalidDataTypeException, QSumInvalidChecksum
from qsum.data import data_checksum
from qsum.data.data_logic import data_digest_from_checksum, resolve_hash_algo

CHECKSUM_OBJS = [Checksum('123'),
                 '0001a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
                 bytes.fromhex('0001a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3')]


class Custom:
    def __init__(self):
        pass


@pytest.mark.xfail(raises=QSumInvalidDataTypeException, strict=True)
def test_invalid_type():
    custom = Custom()
    _ = data_checksum(custom, type(custom), hash_algo=DEFAULT_HASH_ALGO)


@pytest.mark.parametrize('checksum_obj', CHECKSUM_OBJS)
def test_data_digest_from_checksum(checksum_obj):
    data_digest = data_digest_from_checksum(checksum_obj)
    if not isinstance(checksum_obj, str):
        data_digest = data_digest.hex()
    assert data_digest == 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'


@pytest.mark.xfail(raises=QSumInvalidChecksum)
def test_invalid_type_passed_to_data_digest_from_checksum():
    data_digest_from_checksum(123)


def test_consistent_hash_algo_resolution():
    assert resolve_hash_algo('sha256') == resolve_hash_algo(hashlib.sha256)
