from functools import lru_cache

# the maxsize here should be ~ # of common types * # of groupings used (~3)
is_sub_class = lru_cache(maxsize=256)(issubclass)  # pylint: disable=invalid-name
