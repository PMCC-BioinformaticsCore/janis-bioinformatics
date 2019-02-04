from janis_bioinformatics.tools import Gatk3Latest
from janis_bioinformatics.tools import Gatk3Mutect2Base


class Gatk3Mutect2Latest(Gatk3Latest, Gatk3Mutect2Base):
    pass


if __name__ == "__main__":
    print(Gatk3Mutect2Latest().help())
