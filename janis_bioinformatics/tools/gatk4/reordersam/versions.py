from .base import Gatk4ReorderSamBase
from ..versions import Gatk_4_1_4_0


class Gatk4ReorderSam_4_1_4(Gatk_4_1_4_0, Gatk4ReorderSamBase):
    pass


Gatk4ReorderSamLatest = Gatk4ReorderSam_4_1_4

if __name__ == "__main__":
    print(Gatk4ReorderSam_4_1_4().help())
