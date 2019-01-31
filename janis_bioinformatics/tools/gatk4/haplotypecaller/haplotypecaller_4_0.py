from bioinformatics.janis_bioinformatics.tools import Gatk_4_0
from bioinformatics.janis_bioinformatics.tools import Gatk4HaplotypeCallerBase


class Gatk4HaplotypeCaller_4_0(Gatk_4_0, Gatk4HaplotypeCallerBase):
    pass


if __name__ == "__main__":
    print(Gatk4HaplotypeCaller_4_0().help())
