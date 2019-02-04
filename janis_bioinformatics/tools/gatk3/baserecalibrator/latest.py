from janis_bioinformatics.tools import Gatk3Latest
from janis_bioinformatics.tools import Gatk3RecalibratorBase


class Gatk3RecalibratorLatest(Gatk3Latest, Gatk3RecalibratorBase):
    pass


if __name__ == "__main__":
    print(Gatk3RecalibratorLatest().help())
