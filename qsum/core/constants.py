import hashlib
from collections import deque

# the default hash algo to use
DEFAULT_HASH_ALGO = hashlib.sha256

BYTES_IN_PREFIX = 2
DEFAULT_BYTES_IN_DATA = 32
DEFAULT_BYTES_IN_CHECKSUM = BYTES_IN_PREFIX + DEFAULT_BYTES_IN_DATA

# containers we can simple apply a map to
MAPPABLE_CONTAINER_TYPES = {tuple, list, deque}

# containers that require more customized logic
CUSTOM_CONTAINER_TYPES = {dict}

# all supported container types
CONTAINER_TYPES = CUSTOM_CONTAINER_TYPES.union(MAPPABLE_CONTAINER_TYPES)
