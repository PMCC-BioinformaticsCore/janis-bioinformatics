from .base import Gatk4MarkDuplicatesBase
from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_2_0 import Gatk_4_1_2_0
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4MarkDuplicates_4_0(Gatk_4_0_12, Gatk4MarkDuplicatesBase):
    pass


class Gatk4MarkDuplicates_4_1_2(Gatk_4_1_2_0, Gatk4MarkDuplicatesBase):
    pass


class Gatk4MarkDuplicates_4_1_3(Gatk_4_1_3_0, Gatk4MarkDuplicatesBase):
    pass


Gatk4MarkDuplicatesLatest = Gatk4MarkDuplicates_4_1_3

if __name__ == "__main__":
    print(Gatk4MarkDuplicates_4_0().help())
