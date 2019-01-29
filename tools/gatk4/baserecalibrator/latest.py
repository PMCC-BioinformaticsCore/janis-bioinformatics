from bioinformatics.tools.gatk4.baserecalibrator.base import Gatk4BaseRecalibratorBase
from bioinformatics.tools.gatk4.gatk_latest import Gatk4Latest


class Gatk4BaseRecalibratorLatest(Gatk4Latest, Gatk4BaseRecalibratorBase):
    pass

if __name__ == "__main__":
    print(Gatk4BaseRecalibratorLatest().help())
