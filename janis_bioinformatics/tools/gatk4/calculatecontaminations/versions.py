from .base import Gatk4CalculateContaminationBase
from ..versions import Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4CalculateContamination_4_1_2(Gatk_4_1_2_0, Gatk4CalculateContaminationBase):
    pass


class Gatk4CalculateContamination_4_1_3(Gatk_4_1_3_0, Gatk4CalculateContaminationBase):
    pass


class Gatk4CalculateContamination_4_1_4(Gatk_4_1_4_0, Gatk4CalculateContaminationBase):
    pass


Gatk4CalculateContaminationLatest = Gatk4CalculateContamination_4_1_4

if __name__ == "__main__":
    print(Gatk4CalculateContaminationBase().help())
