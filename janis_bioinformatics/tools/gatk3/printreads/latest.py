from bioinformatics.janis_bioinformatics.tools import Gatk3Latest
from bioinformatics.janis_bioinformatics.tools import Gatk3PrintReadsBase


class Gatk3PrintReadsLatest(Gatk3Latest, Gatk3PrintReadsBase):
    pass


if __name__ == "__main__":
    print(Gatk3PrintReadsLatest().help())
