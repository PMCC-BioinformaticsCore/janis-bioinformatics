from .base import Gatk4BaseRecalibratorBase
from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_2_0 import Gatk_4_1_2_0
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4BaseRecalibrator_4_0(Gatk_4_0_12, Gatk4BaseRecalibratorBase):
    pass


class Gatk4BaseRecalibrator_4_1_2(Gatk_4_1_2_0, Gatk4BaseRecalibratorBase):
    pass


class Gatk4BaseRecalibrator_4_1_3(Gatk_4_1_3_0, Gatk4BaseRecalibratorBase):
    pass


Gatk4BaseRecalibratorLatest = Gatk4BaseRecalibrator_4_1_3

if __name__ == "__main__":
    print(Gatk4BaseRecalibrator_4_0().help())
