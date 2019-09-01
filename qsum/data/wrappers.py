def encode_wrapper(func):
    """Wrap a given function in an encode code, useful for add to functions that generate bytes"""

    def inner(*args, **kwargs):
        return func(*args, **kwargs).encode()

    return inner
