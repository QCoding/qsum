from qsum.types.type_map import PREFIX_BYTES


def data_digest_from_checksum(checksum):
    """Extract the data digest bytes from the checksum"""
    return checksum[PREFIX_BYTES:]
