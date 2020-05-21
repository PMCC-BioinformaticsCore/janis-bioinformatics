from .base_cram import Gatk4GetPileUpSummariesBase
from ..versions import Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4GetPileUpSummaries_4_1_2(Gatk_4_1_2_0, Gatk4GetPileUpSummariesBase):
    pass


class Gatk4GetPileUpSummaries_4_1_3(Gatk_4_1_3_0, Gatk4GetPileUpSummariesBase):
    pass


class Gatk4GetPileUpSummaries_4_1_4(Gatk_4_1_4_0, Gatk4GetPileUpSummariesBase):
    pass


Gatk4GetPileUpSummariesLatest = Gatk4GetPileUpSummaries_4_1_4

if __name__ == "__main__":
    print(Gatk4GetPileUpSummariesBase().help())
