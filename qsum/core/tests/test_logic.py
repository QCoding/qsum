import hashlib

import pytest

from qsum.core.constants import BYTES_IN_PREFIX
from qsum.core.logic import is_supported_type, checksum


class NotCheckSummable():
    pass


def test_is_supported_type():
    assert is_supported_type(str)
    assert not is_supported_type(NotCheckSummable)


@pytest.mark.parametrize('hash_algo,hash_length', [
    (hashlib.sha1, 20),
    (hashlib.sha224, 28),
    (hashlib.sha256, 32),
    (hashlib.sha512, 64)])
def test_sha_lengths(hash_algo, hash_length):
    assert len(checksum('123', hash_algo=hash_algo)) == hash_length + BYTES_IN_PREFIX