from .base import Gatk4SortSamBase
from ..gatk_4_0 import Gatk_4_0


class Gatk4SortSam_4_0(Gatk4SortSamBase, Gatk_4_0):
    pass


if __name__ == "__main__":
    print(Gatk4SortSam_4_0().help())