from .base import Gatk4HaplotypeCallerBase
from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_2_0 import Gatk_4_1_2_0
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4HaplotypeCaller_4_0(Gatk_4_0_12, Gatk4HaplotypeCallerBase):
    pass


class Gatk4HaplotypeCaller_4_1_2(Gatk_4_1_2_0, Gatk4HaplotypeCallerBase):
    pass


class Gatk4HaplotypeCaller_4_1_3(Gatk_4_1_3_0, Gatk4HaplotypeCallerBase):
    pass


Gatk4HaplotypeCallerLatest = Gatk4HaplotypeCaller_4_1_3

if __name__ == "__main__":
    print(Gatk4HaplotypeCaller_4_0().help())
