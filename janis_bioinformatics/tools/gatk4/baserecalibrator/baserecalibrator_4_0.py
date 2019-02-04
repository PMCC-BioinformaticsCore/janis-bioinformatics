from .base import Gatk4BaseRecalibratorBase
from ..gatk_4_0 import Gatk_4_0


class Gatk4BaseRecalibrator_4_0(Gatk_4_0, Gatk4BaseRecalibratorBase):
    pass


if __name__ == "__main__":
    print(Gatk4BaseRecalibrator_4_0().help())
