from .base import Gatk4PrintReadsBase
from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4PrintReads_4_0(Gatk_4_0_12, Gatk4PrintReadsBase):
    pass


class Gatk4PrintReads_4_1_3(Gatk_4_1_3_0, Gatk4PrintReadsBase):
    pass


Gatk4PrintReadsLatest = Gatk4PrintReads_4_1_3

if __name__ == "__main__":
    print(Gatk4PrintReads_4_0().help())
