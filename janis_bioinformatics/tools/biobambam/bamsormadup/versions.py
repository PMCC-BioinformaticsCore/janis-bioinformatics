from ..versions import BioBamBam_2_0_87
from .base import BamSorMaDupBase


class BamSorMaDup_2_0_87(BioBamBam_2_0_87, BamSorMaDupBase):
    pass


BamSorMaDupLatest = BamSorMaDup_2_0_87


if __name__ == "__main__":
    print(BamSorMaDupLatest().help())
