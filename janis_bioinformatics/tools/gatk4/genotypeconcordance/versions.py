from .base import Gatk4GenotypeConcordanceBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4GenotypeConcordance_4_0(Gatk_4_0_12, Gatk4GenotypeConcordanceBase):
    pass


class Gatk4GenotypeConcordance_4_1_2(Gatk_4_1_2_0, Gatk4GenotypeConcordanceBase):
    pass


class Gatk4GenotypeConcordance_4_1_3(Gatk_4_1_3_0, Gatk4GenotypeConcordanceBase):
    pass


class Gatk4GenotypeConcordance_4_1_4(Gatk_4_1_4_0, Gatk4GenotypeConcordanceBase):
    pass


Gatk4GenotypeConcordanceLatest = Gatk4GenotypeConcordance_4_1_4

if __name__ == "__main__":
    print(Gatk4GenotypeConcordance_4_0().help())
