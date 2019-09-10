from .base import Gatk4LearnReadOrientationModelBase
from ..gatk_4_1_2_0 import Gatk_4_1_2_0
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4LearnReadOrientationModel_4_1_2(
    Gatk_4_1_2_0, Gatk4LearnReadOrientationModelBase
):
    pass


class Gatk4LearnReadOrientationModel_4_1_3(
    Gatk_4_1_3_0, Gatk4LearnReadOrientationModelBase
):
    pass


Gatk4LearnReadOrientationModelLatest = Gatk4LearnReadOrientationModel_4_1_3

if __name__ == "__main__":
    print(Gatk4LearnReadOrientationModelBase().help())
