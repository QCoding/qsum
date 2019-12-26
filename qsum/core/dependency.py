import typing

from qsum.core.cache import get_package_version


def resolve_dependency(dep):
    """Resolves the value of the dep

    Args:
        dep: for a string of a package name get the package version

    Returns:
        the solved value of the dependency
    """
    return get_package_version(dep)


def resolve_dependencies(depends_on: typing.Collection):
    """Map the individual deps to their resolution

    Args:
        depends_on:
            collection (tuple, list, set, etc.) of python package dependencies

    Returns:
        dictionary mapping the packages to their versions, note changing the type of depends_on should not change the
        output type

    """
    return {d: resolve_dependency(d) for d in depends_on}
