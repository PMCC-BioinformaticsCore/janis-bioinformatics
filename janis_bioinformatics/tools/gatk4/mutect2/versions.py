from .base_4_0 import Gatk4Mutect2Base_4_0
from .base_4_1 import Gatk4Mutect2Base_4_1
from .base_4_1_cram import Gatk4Mutect2CramBase_4_1

from ..versions import (
    Gatk_4_0_12,
    Gatk_4_1_2_0,
    Gatk_4_1_3_0,
    Gatk_4_1_4_0,
    Gatk_4_1_6_0,
    Gatk_4_1_7_0,
    Gatk_4_1_8_1,
)


class GatkMutect2_4_0(Gatk_4_0_12, Gatk4Mutect2Base_4_0):
    pass


class GatkMutect2_4_1_2(Gatk_4_1_2_0, Gatk4Mutect2Base_4_1):
    pass


class GatkMutect2_4_1_3(Gatk_4_1_3_0, Gatk4Mutect2Base_4_1):
    pass


class GatkMutect2_4_1_4(Gatk_4_1_4_0, Gatk4Mutect2Base_4_1):
    pass


class GatkMutect2_4_1_6(Gatk_4_1_6_0, Gatk4Mutect2Base_4_1):
    pass


class GatkMutect2_4_1_7(Gatk_4_1_7_0, Gatk4Mutect2Base_4_1):
    pass


class GatkMutect2_4_1_8(Gatk_4_1_8_1, Gatk4Mutect2Base_4_1):
    pass


# CRAM versions


class GatkMutect2Cram_4_1_2(Gatk_4_1_2_0, Gatk4Mutect2CramBase_4_1):
    pass


class GatkMutect2Cram_4_1_3(Gatk_4_1_3_0, Gatk4Mutect2CramBase_4_1):
    pass


class GatkMutect2Cram_4_1_4(Gatk_4_1_4_0, Gatk4Mutect2CramBase_4_1):
    pass


class GatkMutect2Cram_4_1_6(Gatk_4_1_6_0, Gatk4Mutect2CramBase_4_1):
    pass


class GatkMutect2Cram_4_1_7(Gatk_4_1_7_0, Gatk4Mutect2CramBase_4_1):
    pass


class GatkMutect2Cram_4_1_8(Gatk_4_1_8_1, Gatk4Mutect2CramBase_4_1):
    pass


GatkMutect2Latest = GatkMutect2_4_1_8

if __name__ == "__main__":
    print(GatkMutect2_4_0().help())
