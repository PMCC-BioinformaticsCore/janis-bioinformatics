from ..versions import Bwa_0_7_15
from .base import BwaMemBase


class BwaMem_0_7_15(Bwa_0_7_15, BwaMemBase):
    pass


BwaMemLatest = BwaMem_0_7_15


if __name__ == "__main__":
    print(BwaMemLatest().help())
