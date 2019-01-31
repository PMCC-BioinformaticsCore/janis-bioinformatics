from bioinformatics.janis_bioinformatics.tools import Gatk4Latest
from bioinformatics.janis_bioinformatics.tools import Gatk4MergeSamFilesBase


class Gatk4MergeSamFilesLatest(Gatk4Latest, Gatk4MergeSamFilesBase):
    pass


if __name__ == "__main__":
    print(Gatk4MergeSamFilesLatest().help())
