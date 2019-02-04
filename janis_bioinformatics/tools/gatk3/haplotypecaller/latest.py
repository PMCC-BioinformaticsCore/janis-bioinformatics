from janis_bioinformatics.tools import Gatk3Latest
from janis_bioinformatics.tools.gatk3.haplotypecaller.base import Gatk3HaplotypeCallerBase


class Gatk3HaplotypeCallerLatest(Gatk3Latest, Gatk3HaplotypeCallerBase):
    pass


if __name__ == "__main__":
    print(Gatk3HaplotypeCallerLatest().help())
