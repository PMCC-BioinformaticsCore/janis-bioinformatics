from .base import Gatk4Mutect2Base
from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class GatkMutect2_4_0(Gatk_4_0_12, Gatk4Mutect2Base):
    pass


class GatkMutect2_4_1_3(Gatk_4_1_3_0, Gatk4Mutect2Base):
    pass


GatkMutect2Latest = GatkMutect2_4_1_3

if __name__ == "__main__":
    print(GatkMutect2_4_0().help())
