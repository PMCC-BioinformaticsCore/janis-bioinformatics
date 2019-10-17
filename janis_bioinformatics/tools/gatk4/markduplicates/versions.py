from .base import Gatk4MarkDuplicatesBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4MarkDuplicates_4_0(Gatk_4_0_12, Gatk4MarkDuplicatesBase):
    pass


class Gatk4MarkDuplicates_4_1_2(Gatk_4_1_2_0, Gatk4MarkDuplicatesBase):
    pass


class Gatk4MarkDuplicates_4_1_3(Gatk_4_1_3_0, Gatk4MarkDuplicatesBase):
    pass


class Gatk4MarkDuplicates_4_1_4(Gatk_4_1_4_0, Gatk4MarkDuplicatesBase):
    pass


Gatk4MarkDuplicatesLatest = Gatk4MarkDuplicates_4_1_4

if __name__ == "__main__":
    print(Gatk4MarkDuplicates_4_0().help())
