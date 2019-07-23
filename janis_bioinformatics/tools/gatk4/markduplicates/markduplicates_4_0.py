from .base import Gatk4MarkDuplicatesBase
from ..gatk_4_0_12 import Gatk_4_0_12


class Gatk4MarkDuplicates_4_0(Gatk_4_0_12, Gatk4MarkDuplicatesBase):
    pass


if __name__ == "__main__":
    print(Gatk4MarkDuplicates_4_0().help())
