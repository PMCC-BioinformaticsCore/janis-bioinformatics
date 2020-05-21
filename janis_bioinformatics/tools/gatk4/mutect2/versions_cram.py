from .base_4_1_cram import Gatk4Mutect2Base_4_1

from ..versions import Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class GatkMutect2_4_1_2(Gatk_4_1_2_0, Gatk4Mutect2Base_4_1):
    pass


class GatkMutect2_4_1_3(Gatk_4_1_3_0, Gatk4Mutect2Base_4_1):
    pass


class GatkMutect2_4_1_4(Gatk_4_1_4_0, Gatk4Mutect2Base_4_1):
    pass


GatkMutect2Latest = GatkMutect2_4_1_4

if __name__ == "__main__":
    print(GatkMutect2_4_0().help())
