"""Functions used throughout qsum that maintain a cache"""
import sys
from functools import lru_cache

import pkg_resources

# the maxsize here should be ~ # of common types * # of groupings used (~3)
from qsum.core.constants import UNKNOWN_VERSION

is_sub_class = lru_cache(maxsize=256)(issubclass)  # pylint: disable=invalid-name


# even in a large environment 128 packages that we care about the version of seems reasonable
@lru_cache(maxsize=128)
def get_package_version(package: str) -> str:
    """Extract version from an installed python package

    Args:
        package: name of the package

    Returns:
        version string

    Raises:
        pkg_resources.DistributionNotFound: when the package info can't be located
    """
    if package == 'python':
        return ".".join(map(str, sys.version_info[0:3]))

    return pkg_resources.get_distribution(package).version


# since the environment shouldn't change within a session only need to cache one value
@lru_cache(maxsize=2)
def all_package_versions(include_python_version=True) -> dict:
    """Get all the package names with their versions in the environment

    Args:
        include_python_version: if True then include the version of python itself
    Returns:
        dict mapping package name to package version
    """
    all_packages = {package.project_name: package.version for package in
                    pkg_resources.working_set}  # pylint: disable=not-an-iterable

    # include the version of python itself if requested
    if include_python_version:
        all_packages['python'] = get_package_version('python')

    return all_packages


# Used for calculating both __version__ and internal qsum calls
@lru_cache(maxsize=1)
def qsum_version():
    """Gets the version of qsum"""
    try:
        return pkg_resources.get_distribution('qsum').version
    except pkg_resources.DistributionNotFound:
        return UNKNOWN_VERSION


def clear_caches():  # pragma: no cover
    """Clear all qsum caches"""
    is_sub_class.cache_clear()
    get_package_version.cache_clear()
    all_package_versions.cache_clear()
    qsum_version.cache_clear()
