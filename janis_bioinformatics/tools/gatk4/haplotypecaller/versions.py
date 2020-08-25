from .base import Gatk4HaplotypeCallerBase
from ..versions import (
    Gatk_4_0_12,
    Gatk_4_1_2_0,
    Gatk_4_1_3_0,
    Gatk_4_1_4_0,
    Gatk_4_1_6_0,
    Gatk_4_1_7_0,
    Gatk_4_1_8_1,
)


class Gatk4HaplotypeCaller_4_0(Gatk_4_0_12, Gatk4HaplotypeCallerBase):
    pass


class Gatk4HaplotypeCaller_4_1_2(Gatk_4_1_2_0, Gatk4HaplotypeCallerBase):
    pass


class Gatk4HaplotypeCaller_4_1_3(Gatk_4_1_3_0, Gatk4HaplotypeCallerBase):
    pass


class Gatk4HaplotypeCaller_4_1_4(Gatk_4_1_4_0, Gatk4HaplotypeCallerBase):
    pass


class Gatk4HaplotypeCaller_4_1_6(Gatk_4_1_6_0, Gatk4HaplotypeCallerBase):
    pass


class Gatk4HaplotypeCaller_4_1_7(Gatk_4_1_7_0, Gatk4HaplotypeCallerBase):
    pass


class Gatk4HaplotypeCaller_4_1_8(Gatk_4_1_8_1, Gatk4HaplotypeCallerBase):
    pass


Gatk4HaplotypeCallerLatest = Gatk4HaplotypeCaller_4_1_8

if __name__ == "__main__":
    print(Gatk4HaplotypeCaller_4_1_8().help())
