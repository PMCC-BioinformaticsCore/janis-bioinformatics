from bioinformatics.janis_bioinformatics.tools import Gatk4Latest
from bioinformatics.janis_bioinformatics.tools.gatk4.mutect2.base import Gatk4Mutect2Base


class Gatk4Mutect2Latest(Gatk4Latest, Gatk4Mutect2Base):
    pass


if __name__ == "__main__":
    print(Gatk4Mutect2Latest().help())
