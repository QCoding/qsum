from importlib.metadata import PackageNotFoundError
import pytest

from qsum.core.cache import get_package_version, all_package_versions, is_sub_class, qsum_version, clear_caches


def test_get_package_version_bad_package():
    """Validate that a bad package name raises the expected exception"""
    with pytest.raises(PackageNotFoundError):
        get_package_version('foo')


def test_get_package_version_pytest():
    """Validate we can pull a package version"""
    assert tuple(map(int, get_package_version('pytest').split('.'))) > (4, 4, 0)


def test_package_version_python():
    """Validate the special case of asking for the python version works"""
    assert tuple(map(int, get_package_version('python').split('.'))) > (3, 5, 0)


def test_all_package_versions_include_python_version():
    """Validate the include_python_version argument of all_package_versions"""
    assert 'python' in all_package_versions(include_python_version=True)
    assert 'python' not in all_package_versions(include_python_version=False)


def test_clear_caches():
    """Test that clear_caches indeed clears all the lru_caches"""
    # populate the caches
    is_sub_class(int, object)
    get_package_version('python')
    all_package_versions()
    qsum_version()

    # check that the caches are populated
    assert is_sub_class.cache_info().currsize > 0
    assert get_package_version.cache_info().currsize > 0
    assert all_package_versions.cache_info().currsize > 0
    assert qsum_version.cache_info().currsize > 0

    # clear the caches
    clear_caches()

    # check that the caches are empty
    assert is_sub_class.cache_info().currsize == 0
    assert get_package_version.cache_info().currsize == 0
    assert all_package_versions.cache_info().currsize == 0
    assert qsum_version.cache_info().currsize == 0
