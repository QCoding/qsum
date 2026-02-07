import sys

from qsum.core.cache import get_package_version, all_package_versions, qsum_version
from qsum.core.constants import DependsOnType, DependsOn, UNKNOWN_VERSION
from qsum.core.exceptions import QSumInvalidDependsOn, QSumUnknownVersionDependency


def resolve_dependency(dep):
    """Resolves the value of the dep

    Args:
        dep: for a string of a package name get the package version

    Returns:
        the solved value of the dependency
    """
    # Interpret strings as package names
    if isinstance(dep, str):
        return get_package_version(dep)

    # Custom case each DependsOn value
    if isinstance(dep, DependsOn):
        if dep == DependsOn.PythonEnv:
            return all_package_versions()
        if dep == DependsOn.PythonVer:
            return get_package_version('python')
        if dep == DependsOn.Platform:
            return sys.platform
        if dep == DependsOn.QSumVer:
            qsum_resolved_version = qsum_version()
            if qsum_resolved_version == UNKNOWN_VERSION:
                raise QSumUnknownVersionDependency()  # pragma: no cover
            return qsum_resolved_version  # pragma: no cover

    raise QSumInvalidDependsOn("{} is not a valid dependency to resolve")


def resolve_dependencies(depends_on: DependsOnType):
    """Map the individual deps to their resolution

    Args:
        depends_on:
            collection (tuple, list, set, etc.) of python package dependencies

    Returns:
        dictionary mapping the packages to their versions, note changing the type of depends_on should not change the
        output type

    """
    # support a single DependsOn value
    if isinstance(depends_on, DependsOn):
        depends_on = [d for d in DependsOn if (depends_on & d) == d]

    return {d: resolve_dependency(d) for d in depends_on}
