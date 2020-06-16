from ..versions import Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0
from .base import Gatk4LearnReadOrientationModelBase


class Gatk4LearnReadOrientationModel_4_1_2(
    Gatk_4_1_2_0, Gatk4LearnReadOrientationModelBase
):
    pass


class Gatk4LearnReadOrientationModel_4_1_3(
    Gatk_4_1_3_0, Gatk4LearnReadOrientationModelBase
):
    pass


class Gatk4LearnReadOrientationModel_4_1_4(
    Gatk_4_1_4_0, Gatk4LearnReadOrientationModelBase
):
    pass


Gatk4LearnReadOrientationModelLatest = Gatk4LearnReadOrientationModel_4_1_4

if __name__ == "__main__":
    print(Gatk4LearnReadOrientationModelBase().help())
