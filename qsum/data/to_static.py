"""
Static checksums should be used for common types with only a few possible values or for certain frequent value or
for difficult cases that are better hard coded

Often these will be generated using the pattern:

>>> from qsum.data.to_bytes import repr_to_bytes
>>> from qsum.data.logic import bytes_to_digest
>>> digest = bytes_to_digest(repr_to_bytes(0.0))
>>> len(digest)
32
"""

from qsum.core.exceptions import QSumStaticLookupMissException

OBJ_TO_CHECKSUM = {}

BOOL_TO_CHECKSUM = {
    True: b"<\xbc\x87\xc7h\x1f4\xdbF\x17\xfe\xaa,\x88\x01\x93\x1b\xc5\xe4-\x8d\x0fV\x0eum\xd4\xcd\x92\x88_\x18",
    False: b"`\xa3>l\xf5\x15\x1f-R\xed\xda\xe9h\\\xfa'\x04&\xaa\x89\xd8\xdb\xc7\xdf\xb8T`o\x1d\x1a@\xfe",
}

FLOAT_TO_CHECKSUM = {
    # cache the checksum for 0.0 for two reasons, first it is a number that will occur extremely often
    # second we want to make sure 0.0 and -0.0 have the same checksum since they are __eq__ but have different __repr__
    0.0: b"\x8a\xedd+\xf5\x11\x8b\x9d<\x85\x9b\xd4\xbe5\xec\xacu\xb6\xe8s\xcc\xe3N{oUK\x06\xf7UP\xd7"
}

# Combine all the individual dicts in to one map so we can verify uniqueness
OBJ_TO_CHECKSUM.update(BOOL_TO_CHECKSUM)
OBJ_TO_CHECKSUM.update(FLOAT_TO_CHECKSUM)


def bool_to_static(obj):
    """Lookup against the smaller bool dict which may be faster then looking up against the full static dict"""
    try:
        return BOOL_TO_CHECKSUM.get(obj)
    except KeyError as e:
        raise QSumStaticLookupMissException("{} does not have a valid static bool checksum".format(obj))


def obj_to_static(obj):
    """Look up the static checksum for a given object against the full map"""
    try:
        return OBJ_TO_CHECKSUM.get(obj)
    except KeyError as e:
        raise QSumStaticLookupMissException("{} does not have a valid static checksum".format(obj))
