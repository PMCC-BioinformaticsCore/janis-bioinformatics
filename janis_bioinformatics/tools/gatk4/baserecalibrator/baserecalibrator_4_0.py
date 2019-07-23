from .base import Gatk4BaseRecalibratorBase
from ..gatk_4_0_12 import Gatk_4_0_12


class Gatk4BaseRecalibrator_4_0(Gatk_4_0_12, Gatk4BaseRecalibratorBase):
    pass


if __name__ == "__main__":
    print(Gatk4BaseRecalibrator_4_0().help())
