from .base import Gatk4GetPileUpSummariesBase
from ..gatk_4_1_2_0 import Gatk_4_1_2_0
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4GetPileUpSummaries_4_1_2(Gatk_4_1_2_0, Gatk4GetPileUpSummariesBase):
    pass


class Gatk4GetPileUpSummaries_4_1_3(Gatk_4_1_3_0, Gatk4GetPileUpSummariesBase):
    pass


Gatk4GetPileUpSummariesLatest = Gatk4GetPileUpSummaries_4_1_3

if __name__ == "__main__":
    print(Gatk4GetPileUpSummariesBase().help())
