from bioinformatics.janis_bioinformatics.tools import Gatk4Latest
from bioinformatics.janis_bioinformatics.tools import Gatk4GenotypeConcordanceBase


class Gatk4GenotypeConcordanceLatest(Gatk4Latest, Gatk4GenotypeConcordanceBase):
    pass


if __name__ == "__main__":
    print(Gatk4GenotypeConcordanceLatest().help())
