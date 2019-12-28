# pylint: disable=invalid-name

# BE REALLY CAREFUL WHAT YOU IMPORT HERE, constants should be lowest level module
import hashlib
import types
import typing
from collections import deque

# the default hash algo to use
DEFAULT_HASH_ALGO = hashlib.sha256

# whether to allow unregistered types by default
DEFAULT_ALLOW_UNREGISTERED = True

BYTES_IN_PREFIX = 2  # type: int
DEFAULT_BYTES_IN_DATA = 32  # type: int
DEFAULT_BYTES_IN_CHECKSUM = BYTES_IN_PREFIX + DEFAULT_BYTES_IN_DATA  # type: int

# containers we can simple apply a map to
MAPPABLE_CONTAINER_TYPES = (tuple, list, deque, set, frozenset)  # type: tuple

# containers we'll have to apply sorting to before hashing
UNORDERED_CONTAINER_TYPES = (set, frozenset, dict)  # type: tuple

# containers that require more customized logic
CUSTOM_CONTAINER_TYPES = (dict,)  # type: tuple

# all supported container types
CONTAINER_TYPES = CUSTOM_CONTAINER_TYPES + MAPPABLE_CONTAINER_TYPES  # type: tuple

# all special types implemented in _checksum code
SPECIAL_TYPES = (types.FunctionType,)

# Used for typing in places where we can't impor the class directly
CHECKSUM_CLASS_NAME = 'Checksum'

# a checksum can be represented by a Checksum object, bytes or a hexidecimal string
ChecksumType = typing.Union[CHECKSUM_CLASS_NAME, bytes, str]

# hash algo can be a str of a method in hashlib or the callable itself
HashAlgoType = typing.Union['str', typing.Callable]

# depends on types
DependsOnType = typing.Optional[typing.Union[tuple, list, set]]


class ChecksumCollection:  # pylint: disable=too-few-public-methods
    """Dummy class to provide a type for combined checksums"""
