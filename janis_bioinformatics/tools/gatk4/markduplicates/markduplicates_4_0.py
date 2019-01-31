from bioinformatics.janis_bioinformatics.tools import Gatk_4_0
from bioinformatics.janis_bioinformatics.tools import Gatk4MarkDuplicatesBase


class Gatk4MarkDuplicates_4_0(Gatk_4_0, Gatk4MarkDuplicatesBase):
    pass


if __name__ == "__main__":
    print(Gatk4MarkDuplicates_4_0().help())
