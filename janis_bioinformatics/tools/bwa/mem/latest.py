from ..bwalatest import BwaLatest
from .base import BwaMemBase


class BwaMemLatest(BwaLatest, BwaMemBase):
    pass


if __name__ == "__main__":
    print(BwaMemLatest().help())
