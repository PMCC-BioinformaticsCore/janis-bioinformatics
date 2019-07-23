from .base import Gatk4MergeSamFilesBase
from ..gatk_4_0_12 import Gatk_4_0_12


class Gatk4MergeSamFiles_4_0(Gatk_4_0_12, Gatk4MergeSamFilesBase):
    pass


if __name__ == "__main__":
    print(Gatk4MergeSamFiles_4_0().help())
