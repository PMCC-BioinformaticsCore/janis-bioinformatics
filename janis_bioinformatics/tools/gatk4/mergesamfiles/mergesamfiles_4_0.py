from .base import Gatk4MergeSamFilesBase
from ..gatk_4_0 import Gatk_4_0


class Gatk4MergeSamFiles_4_0(Gatk_4_0, Gatk4MergeSamFilesBase):
    pass


if __name__ == "__main__":
    print(Gatk4MergeSamFiles_4_0().help())
