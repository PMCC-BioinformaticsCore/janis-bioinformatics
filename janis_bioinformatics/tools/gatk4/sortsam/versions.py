from .base import Gatk4SortSamBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4SortSam_4_0(Gatk_4_0_12, Gatk4SortSamBase):
    pass


class Gatk4SortSam_4_1_2(Gatk_4_1_2_0, Gatk4SortSamBase):
    pass


class Gatk4SortSam_4_1_3(Gatk_4_1_3_0, Gatk4SortSamBase):
    pass


class Gatk4SortSam_4_1_4(Gatk_4_1_4_0, Gatk4SortSamBase):
    pass


Gatk4SortSamLatest = Gatk4SortSam_4_1_4

if __name__ == "__main__":
    print(Gatk4SortSam_4_0().help())
