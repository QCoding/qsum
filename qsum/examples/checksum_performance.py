from time import time

from qsum import checksum


class Timer:
    """Adopted from https://blog.usejournal.com/how-to-create-your-own-timing-context-manager-in-python-a0e944b48cf8"""

    def __init__(self, description):
        self.description = description
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time()

    def __exit__(self, *args):
        self.end = time()
        print("{}: {:.6f}s".format(self.description, self.end - self.start))


def main():
    """Example of computing a lot of checksums"""
    with Timer("Computing 1000000 checksums"):
        lots_of_ints = range(0, 1000000)
        checksums = list(map(checksum, lots_of_ints))
    assert len(checksums) == len(lots_of_ints)


if __name__ == "__main__":
    main()
