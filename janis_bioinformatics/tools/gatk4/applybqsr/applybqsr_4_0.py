from .base import Gatk4ApplyBqsrBase
from ..gatk_4_0_12 import Gatk_4_0_12


class Gatk4ApplyBqsr_4_0(Gatk_4_0_12, Gatk4ApplyBqsrBase):
    pass


if __name__ == "__main__":
    print(Gatk4ApplyBqsr_4_0().help())
