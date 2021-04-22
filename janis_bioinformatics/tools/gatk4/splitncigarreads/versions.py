from .base import Gatk4SplitNCigarReadsBase
from ..versions import (
    Gatk_4_0_12,
    Gatk_4_1_2_0,
    Gatk_4_1_3_0,
    Gatk_4_1_4_0,
    Gatk_4_1_8_1,
)


class Gatk4SplitNCigarReads_4_0(Gatk_4_0_12, Gatk4SplitNCigarReadsBase):
    pass


class Gatk4SplitNCigarReads_4_1_2(Gatk_4_1_2_0, Gatk4SplitNCigarReadsBase):
    pass


class Gatk4SplitNCigarReads_4_1_3(Gatk_4_1_3_0, Gatk4SplitNCigarReadsBase):
    pass


class Gatk4SplitNCigarReads_4_1_4(Gatk_4_1_4_0, Gatk4SplitNCigarReadsBase):
    pass


class Gatk4SplitNCigarReads_4_1_8_1(Gatk_4_1_8_1, Gatk4SplitNCigarReadsBase):
    pass


Gatk4SplitNCigarReadsLatest = Gatk4SplitNCigarReads_4_1_8_1

if __name__ == "__main__":
    print(Gatk4SplitNCigarReadsLatest().help())
