from .base import Gatk4SelectVariantsBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4SelectVariants_4_0(Gatk_4_0_12, Gatk4SelectVariantsBase):
    pass


class Gatk4SelectVariants_4_1_2(Gatk_4_1_2_0, Gatk4SelectVariantsBase):
    pass


class Gatk4SelectVariants_4_1_3(Gatk_4_1_3_0, Gatk4SelectVariantsBase):
    pass


class Gatk4SelectVariants_4_1_4(Gatk_4_1_4_0, Gatk4SelectVariantsBase):
    pass


Gatk4SelectVariantsLatest = Gatk4SelectVariants_4_1_4

if __name__ == "__main__":
    print(Gatk4SelectVariants_4_0().help())
