from bioinformatics.janis_bioinformatics.tools import Gatk_4_0
from bioinformatics.janis_bioinformatics.tools import Gatk4GenotypeConcordanceBase


class Gatk4GenotypeConcordance_4_0(Gatk_4_0, Gatk4GenotypeConcordanceBase):
    pass


if __name__ == "__main__":
    print(Gatk4GenotypeConcordance_4_0().help())
