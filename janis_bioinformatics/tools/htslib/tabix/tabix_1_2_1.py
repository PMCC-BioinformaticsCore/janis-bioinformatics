from .base import TabixBase
from ..htslib_1_2_1 import HTSLib_1_2_1


class Tabix_1_2_1(HTSLib_1_2_1, TabixBase):
    pass


if __name__ == "__main__":
    print(Tabix_1_2_1().help())
