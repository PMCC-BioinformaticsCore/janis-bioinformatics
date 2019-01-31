from bioinformatics.janis_bioinformatics.tools import Gatk4BaseRecalibratorBase
from bioinformatics.janis_bioinformatics.tools import Gatk4Latest


class Gatk4BaseRecalibratorLatest(Gatk4Latest, Gatk4BaseRecalibratorBase):
    pass

if __name__ == "__main__":
    print(Gatk4BaseRecalibratorLatest().help())
