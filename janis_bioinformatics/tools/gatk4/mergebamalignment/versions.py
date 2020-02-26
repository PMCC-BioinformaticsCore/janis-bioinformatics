from .base import Gatk4MergeBamAlignmentBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0, Gatk_4_1_4_1


class Gatk4MergeBamAlignment_4_0(Gatk_4_0_12, Gatk4MergeBamAlignmentBase):
    pass


class Gatk4MergeBamAlignment_4_1_2(Gatk_4_1_2_0, Gatk4MergeBamAlignmentBase):
    pass


class Gatk4MergeBamAlignment_4_1_3(Gatk_4_1_3_0, Gatk4MergeBamAlignmentBase):
    pass


class Gatk4MergeBamAlignment_4_1_4(Gatk_4_1_4_1, Gatk4MergeBamAlignmentBase):
    pass


Gatk4MergeBamAlignmentLatest = Gatk4MarkDuplicates_4_1_4

if __name__ == "__main__":
    print(Gatk4MergeBamAlignmentLatest().help())
