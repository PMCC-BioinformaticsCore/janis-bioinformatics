from .base import Gatk4MergeMutectStatsBase
from ..gatk_4_1_2_0 import Gatk_4_1_2_0
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4MergeMutectStats_4_1_2(Gatk_4_1_2_0, Gatk4MergeMutectStatsBase):
    pass


class Gatk4MergeMutectStats_4_1_3(Gatk_4_1_3_0, Gatk4MergeMutectStatsBase):
    pass


Gatk4MergeMutectStatsLatest = Gatk4MergeMutectStats_4_1_3

if __name__ == "__main__":
    print(Gatk4MergeMutectStatsBase().help())
