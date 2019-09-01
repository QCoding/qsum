from qsum.core.exceptions import QSumStaticLookupMissException

OBJ_TO_CHECKSUM = {}

BOOL_TO_CHECKSUM = {
    True: b"<\xbc\x87\xc7h\x1f4\xdbF\x17\xfe\xaa,\x88\x01\x93\x1b\xc5\xe4-\x8d\x0fV\x0eum\xd4\xcd\x92\x88_\x18",
    False: b"`\xa3>l\xf5\x15\x1f-R\xed\xda\xe9h\\\xfa'\x04&\xaa\x89\xd8\xdb\xc7\xdf\xb8T`o\x1d\x1a@\xfe",
}

# Combine all the individual dicts in to one map so we can verify uniqueness
OBJ_TO_CHECKSUM.update(BOOL_TO_CHECKSUM)


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
