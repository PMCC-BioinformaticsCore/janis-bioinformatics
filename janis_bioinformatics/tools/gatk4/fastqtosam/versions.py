from .base import Gatk4FastqToSamBase
from ..versions import (
    Gatk_4_0_12,
    Gatk_4_1_2_0,
    Gatk_4_1_3_0,
    Gatk_4_1_4_0,
    Gatk_4_1_4_1,
)


class Gatk4FastqToSam_4_0(Gatk_4_0_12, Gatk4FastqToSamBase):
    pass


class Gatk4FastqToSam_4_1_2(Gatk_4_1_2_0, Gatk4FastqToSamBase):
    pass


class Gatk4FastqToSam_4_1_3(Gatk_4_1_3_0, Gatk4FastqToSamBase):
    pass


class Gatk4FastqToSam_4_1_4(Gatk_4_1_4_1, Gatk4FastqToSamBase):
    pass


Gatk4FastqToSamLatest = Gatk4FastqToSam_4_1_4

if __name__ == "__main__":
    print(Gatk4FastqToSamLatest().help())
