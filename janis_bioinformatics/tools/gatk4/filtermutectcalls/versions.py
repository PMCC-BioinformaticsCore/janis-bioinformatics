from .base import Gatk4FilterMutectCallsBase
from ..versions import (
    Gatk_4_1_2_0,
    Gatk_4_1_3_0,
    Gatk_4_1_4_0,
    Gatk_4_1_6_0,
    Gatk_4_1_7_0,
    Gatk_4_1_8_1,
)


class Gatk4FilterMutectCalls_4_1_2(Gatk_4_1_2_0, Gatk4FilterMutectCallsBase):
    pass


class Gatk4FilterMutectCalls_4_1_3(Gatk_4_1_3_0, Gatk4FilterMutectCallsBase):
    pass


class Gatk4FilterMutectCalls_4_1_4(Gatk_4_1_4_0, Gatk4FilterMutectCallsBase):
    pass


class Gatk4FilterMutectCalls_4_1_6(Gatk_4_1_6_0, Gatk4FilterMutectCallsBase):
    pass


class Gatk4FilterMutectCalls_4_1_7(Gatk_4_1_7_0, Gatk4FilterMutectCallsBase):
    pass


class Gatk4FilterMutectCalls_4_1_8(Gatk_4_1_8_1, Gatk4FilterMutectCallsBase):
    pass


Gatk4FilterMutectCallsLatest = Gatk4FilterMutectCalls_4_1_8

if __name__ == "__main__":
    print(Gatk4FilterMutectCallsBase().help())
