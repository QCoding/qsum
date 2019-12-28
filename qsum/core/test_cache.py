import pkg_resources
import pytest

from qsum.core.cache import get_package_version


@pytest.mark.xfail(raises=pkg_resources.DistributionNotFound, strict=True)
def test_get_package_version_bad_package():
    """Validate that a bad package name raises the expected exception"""
    get_package_version('foo')


def test_get_package_version_pytest():
    """Validate we can pull a package version"""
    assert tuple(map(int, get_package_version('pytest').split('.'))) > (4, 4, 0)


def test_package_version_python():
    """Validate the special case of asking for the python version works"""
    assert tuple(map(int, get_package_version('python').split('.'))) > (3, 5, 0)
