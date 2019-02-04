from ..bwa_0_7_15 import Bwa_0_7_15
from .base import BwaMemBase


class BwaMem_0_7_15(Bwa_0_7_15, BwaMemBase):
    pass


if __name__ == "__main__":
    print(BwaMem_0_7_15().help())
