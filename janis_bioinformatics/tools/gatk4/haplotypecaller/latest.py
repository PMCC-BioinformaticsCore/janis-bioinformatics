from bioinformatics.janis_bioinformatics.tools import Gatk4Latest
from bioinformatics.janis_bioinformatics.tools import Gatk4HaplotypeCallerBase


class Gatk4HaplotypeCallerLatest(Gatk4Latest, Gatk4HaplotypeCallerBase):
    pass


if __name__ == "__main__":
    print(Gatk4HaplotypeCallerLatest().help())
