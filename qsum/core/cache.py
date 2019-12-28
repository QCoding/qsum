"""Functions used throughout qsum that maintain a cache"""
import sys
from functools import lru_cache

import pkg_resources

# the maxsize here should be ~ # of common types * # of groupings used (~3)
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
@lru_cache(maxsize=1)
def all_package_versions() -> dict:
    """Get all the package names with their versions in the environment
    Returns:
        dict mapping package name to package version
    """
    return {package.project_name: package.version for package in
            pkg_resources.working_set}  # pylint: disable=not-an-iterable
