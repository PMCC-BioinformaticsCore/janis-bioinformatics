from .base import Gatk4Mutect2Base
from ..gatk_4_0_12 import Gatk_4_0_12


class GatkMutect2_4_0(Gatk_4_0_12, Gatk4Mutect2Base):
    pass


if __name__ == "__main__":
    print(GatkMutect2_4_0().help())
