from bioinformatics.janis_bioinformatics.tools import Gatk_4_0
from bioinformatics.janis_bioinformatics.tools import Gatk4BaseRecalibratorBase


class Gatk4BaseRecalibrator_4_0(Gatk_4_0, Gatk4BaseRecalibratorBase):
    pass


if __name__ == "__main__":
    print(Gatk4BaseRecalibrator_4_0().help())
