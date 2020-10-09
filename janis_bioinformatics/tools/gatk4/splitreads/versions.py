from .base import Gatk4SplitReadsBase
from ..versions import Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4SplitReads_4_1_2(Gatk_4_1_2_0, Gatk4SplitReadsBase):
    pass


class Gatk4SplitReads_4_1_3(Gatk_4_1_3_0, Gatk4SplitReadsBase):
    pass


class Gatk4SplitReads_4_1_4(Gatk_4_1_4_0, Gatk4SplitReadsBase):
    pass


Gatk4SplitReadsLatest = Gatk4SplitReads_4_1_4

if __name__ == "__main__":
    print(Gatk4SplitReads_4_1_4().help())
