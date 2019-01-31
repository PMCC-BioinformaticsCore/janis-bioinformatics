from bioinformatics.janis_bioinformatics.tools import Gatk4Latest
from bioinformatics.janis_bioinformatics.tools import Gatk4SortSamBase


class Gatk4SortSamLatest(Gatk4Latest, Gatk4SortSamBase):
    pass


if __name__ == "__main__":
    print(Gatk4SortSamLatest().help())
