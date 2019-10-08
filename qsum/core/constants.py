# pylint: disable=invalid-name
import hashlib
from collections import deque

# the default hash algo to use
DEFAULT_HASH_ALGO = hashlib.sha256

BYTES_IN_PREFIX = 2
DEFAULT_BYTES_IN_DATA = 32
DEFAULT_BYTES_IN_CHECKSUM = BYTES_IN_PREFIX + DEFAULT_BYTES_IN_DATA

# containers we can simple apply a map to
MAPPABLE_CONTAINER_TYPES: set = {tuple, list, deque, set, frozenset}

# containers we'll have to apply sorting to before hashing
UNORDERED_CONTAINER_TYPES = {set, frozenset, dict}

# containers that require more customized logic
CUSTOM_CONTAINER_TYPES: set = {dict}

# all supported container types
CONTAINER_TYPES = CUSTOM_CONTAINER_TYPES.union(MAPPABLE_CONTAINER_TYPES)
