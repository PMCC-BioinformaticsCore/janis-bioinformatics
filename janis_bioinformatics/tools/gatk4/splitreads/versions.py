from .base import Gatk4SplitReadsBase
from ..gatk_4_1_2_0 import Gatk_4_1_2_0
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4SplitReads_4_1_2(Gatk_4_1_2_0, Gatk4SplitReadsBase):
    pass


class Gatk4SplitReads_4_1_3(Gatk_4_1_3_0, Gatk4SplitReadsBase):
    pass


Gatk4SortSamLatest = Gatk4SplitReads_4_1_3

if __name__ == "__main__":
    print(Gatk4SplitReads_4_1_3().help())
