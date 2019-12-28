from qsum.core.cache import get_package_version, all_package_versions
from qsum.core.constants import DependsOnType, DependsOn
from qsum.core.exceptions import QSumInvalidDependsOn


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
    if dep == DependsOn.PythonEnv:
        return all_package_versions()

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
        depends_on = (depends_on,)

    return {d: resolve_dependency(d) for d in depends_on}
