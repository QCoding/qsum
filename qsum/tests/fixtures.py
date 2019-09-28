import pytest


@pytest.fixture(scope='session')
def range_2_16():
    """Create a range fixture for use in pytests"""
    return range(-2 ** 16, 2 ** 16)
