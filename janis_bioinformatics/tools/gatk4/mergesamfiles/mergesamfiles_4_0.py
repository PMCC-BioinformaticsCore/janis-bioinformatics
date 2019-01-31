from bioinformatics.janis_bioinformatics.tools import Gatk_4_0
from bioinformatics.janis_bioinformatics.tools import Gatk4MergeSamFilesBase


class Gatk4MergeSamFiles_4_0(Gatk_4_0, Gatk4MergeSamFilesBase):
    pass


if __name__ == "__main__":
    print(Gatk4MergeSamFiles_4_0().help())
