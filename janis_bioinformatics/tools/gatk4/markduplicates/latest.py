from bioinformatics.janis_bioinformatics.tools import Gatk4Latest
from bioinformatics.janis_bioinformatics.tools import Gatk4MarkDuplicatesBase


class Gatk4MarkDuplicatesLatest(Gatk4Latest, Gatk4MarkDuplicatesBase):
    pass

if __name__ == "__main__":
    print(Gatk4MarkDuplicatesLatest().help())
