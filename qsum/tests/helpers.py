import pytest

from qsum import Checksum

STR_CHECKSUM_OBJS = [Checksum('123'),
                     '0001a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
                     bytes.fromhex('0001a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3')]
INT_CHECKSUM_OBJS = [Checksum(123), '0000a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
                     bytes.fromhex('0000a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3')]


@pytest.fixture(scope='session')
def range_2_16():
    """Create a range fixture for use in pytests"""
    return range(-2 ** 16, 2 ** 16)
