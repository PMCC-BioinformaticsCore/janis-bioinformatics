from .base_4_0 import Gatk4Mutect2Base_4_0
from .base_4_1 import Gatk4Mutect2Base_4_1

from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_2_0 import Gatk_4_1_2_0
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class GatkMutect2_4_0(Gatk_4_0_12, Gatk4Mutect2Base_4_0):
    pass


class GatkMutect2_4_1_2(Gatk_4_1_2_0, Gatk4Mutect2Base_4_1):
    pass


class GatkMutect2_4_1_3(Gatk_4_1_3_0, Gatk4Mutect2Base_4_1):
    pass


GatkMutect2Latest = GatkMutect2_4_1_3

if __name__ == "__main__":
    print(GatkMutect2_4_0().help())
