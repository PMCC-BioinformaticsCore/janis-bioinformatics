from .base import GatkSplitNCigarReadsBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class GatkSplitNCigarReads_4_0(Gatk_4_0_12, GatkSplitNCigarReadsBase):
    pass


class GatkSplitNCigarReads_4_1_2(Gatk_4_1_2_0, GatkSplitNCigarReadsBase):
    pass


class GatkSplitNCigarReads_4_1_3(Gatk_4_1_3_0, GatkSplitNCigarReadsBase):
    pass


class GatkSplitNCigarReads_4_1_4(Gatk_4_1_4_0, GatkSplitNCigarReadsBase):
    pass


GatkSplitNCigarReadsLatest = GatkSplitNCigarReads_4_1_4

if __name__ == "__main__":
    print(GatkSplitNCigarReadsLatest().help())
