from .base import Gatk4FilterMutectCallsBase
from ..versions import Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4FilterMutectCalls_4_1_2(Gatk_4_1_2_0, Gatk4FilterMutectCallsBase):
    pass


class Gatk4FilterMutectCalls_4_1_3(Gatk_4_1_3_0, Gatk4FilterMutectCallsBase):
    pass


class Gatk4FilterMutectCalls_4_1_4(Gatk_4_1_4_0, Gatk4FilterMutectCallsBase):
    pass


Gatk4FilterMutectCallsLatest = Gatk4FilterMutectCalls_4_1_3

if __name__ == "__main__":
    print(Gatk4FilterMutectCallsBase().help())
