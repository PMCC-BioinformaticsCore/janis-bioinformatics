from bioinformatics.janis_bioinformatics.tools.gatk4.gatk_4_0 import Gatk_4_0
from bioinformatics.janis_bioinformatics.tools.gatk4.sortsam.base import Gatk4SortSamBase


class Gatk4SortSam_4_0(Gatk4SortSamBase, Gatk_4_0):
    pass


if __name__ == "__main__":
    print(Gatk4SortSam_4_0().help())