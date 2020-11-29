from .base import Gatk4MergeMutectStatsBase
from ..versions import (
    Gatk_4_1_2_0,
    Gatk_4_1_3_0,
    Gatk_4_1_4_0,
    Gatk_4_1_6_0,
    Gatk_4_1_7_0,
    Gatk_4_1_8_0,
)


class Gatk4MergeMutectStats_4_1_2(Gatk_4_1_2_0, Gatk4MergeMutectStatsBase):
    pass


class Gatk4MergeMutectStats_4_1_3(Gatk_4_1_3_0, Gatk4MergeMutectStatsBase):
    pass


class Gatk4MergeMutectStats_4_1_4(Gatk_4_1_4_0, Gatk4MergeMutectStatsBase):
    pass


class Gatk4MergeMutectStats_4_1_6(Gatk_4_1_6_0, Gatk4MergeMutectStatsBase):
    pass


class Gatk4MergeMutectStats_4_1_7(Gatk_4_1_7_0, Gatk4MergeMutectStatsBase):
    pass


class Gatk4MergeMutectStats_4_1_8(Gatk_4_1_8_0, Gatk4MergeMutectStatsBase):
    pass


Gatk4MergeMutectStatsLatest = Gatk4MergeMutectStats_4_1_8

if __name__ == "__main__":
    print(Gatk4MergeMutectStatsBase().help())
