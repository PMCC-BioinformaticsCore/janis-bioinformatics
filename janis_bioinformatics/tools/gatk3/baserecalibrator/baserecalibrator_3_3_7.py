from janis_bioinformatics.tools import Gatk3RecalibratorBase
from janis_bioinformatics.tools import Gatk_3_3_7


class Gatk3BaseRecalibrator_3_3_7(Gatk_3_3_7, Gatk3RecalibratorBase):
    pass


if __name__ == "__main__":
    print(Gatk3BaseRecalibrator_3_3_7().help())
