from .base import Gatk4VariantFiltrationBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4VariantFiltration_4_0(Gatk_4_0_12, Gatk4VariantFiltrationBase):
    pass


class Gatk4VariantFiltration_4_1_2(Gatk_4_1_2_0, Gatk4VariantFiltrationBase):
    pass


class Gatk4VariantFiltration_4_1_3(Gatk_4_1_3_0, Gatk4VariantFiltrationBase):
    pass


class Gatk4VariantFiltration_4_1_4(Gatk_4_1_4_0, Gatk4VariantFiltrationBase):
    pass


Gatk4VariantFiltrationLatest = Gatk4VariantFiltration_4_1_4

if __name__ == "__main__":
    print(Gatk4VariantFiltrationLatest().help())
