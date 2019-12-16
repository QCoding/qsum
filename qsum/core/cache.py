from functools import lru_cache

# the maxsize here should be ~ # of common types * # of groupings used (~3)
@lru_cache(maxsize=256)
def is_sub_class(c, class_info):
    return issubclass(c, class_info)
