from .base import Gatk4MergeSamFilesBase
from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4MergeSamFiles_4_0(Gatk_4_0_12, Gatk4MergeSamFilesBase):
    pass


class Gatk4MergeSamFiles_4_1_3(Gatk_4_1_3_0, Gatk4MergeSamFilesBase):
    pass


Gatk4MergeSamFilesLatest = Gatk4MergeSamFiles_4_1_3

if __name__ == "__main__":
    print(Gatk4MergeSamFiles_4_0().help())
