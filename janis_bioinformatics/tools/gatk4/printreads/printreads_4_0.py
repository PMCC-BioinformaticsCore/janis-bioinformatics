from .base import Gatk4PrintReadsBase
from ..gatk_4_0_12 import Gatk_4_0_12


class Gatk4PrintReads_4_0(Gatk_4_0_12, Gatk4PrintReadsBase):
    pass

if __name__ == "__main__":
    print(Gatk4PrintReads_4_0().help())
