from janis_bioinformatics.tools import Gatk_3_3_7
from janis_bioinformatics.tools import Gatk3Mutect2Base


class Gatk3Mutect2_3_3_7(Gatk_3_3_7, Gatk3Mutect2Base):
    pass


if __name__ == "__main__":
    print(Gatk3Mutect2_3_3_7().help())
