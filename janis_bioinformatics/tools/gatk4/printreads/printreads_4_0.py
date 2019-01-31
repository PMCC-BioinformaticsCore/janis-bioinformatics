from bioinformatics.janis_bioinformatics.tools import Gatk_4_0
from bioinformatics.janis_bioinformatics.tools import Gatk4PrintReadsBase


class Gatk4PrintReads_4_0(Gatk_4_0, Gatk4PrintReadsBase):
    pass

if __name__ == "__main__":
    print(Gatk4PrintReads_4_0().help())
