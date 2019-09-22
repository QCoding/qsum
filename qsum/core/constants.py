BYTES_IN_PREFIX = 2
BYTES_IN_DATA = 32
BYTES_IN_CHECKSUM = BYTES_IN_PREFIX + BYTES_IN_DATA

# containers we can simple apply a map to
MAPPABLE_CONTAINER_TYPES = {tuple,list}

# all supported container types
CONTAINER_TYPES = MAPPABLE_CONTAINER_TYPES
