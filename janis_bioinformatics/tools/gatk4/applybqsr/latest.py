from bioinformatics.janis_bioinformatics.tools import Gatk4ApplyBqsrBase
from bioinformatics.janis_bioinformatics.tools import Gatk4Latest


class Gatk4ApplyBqsrLatest(Gatk4Latest, Gatk4ApplyBqsrBase):
    pass


if __name__ == "__main__":
    print(Gatk4ApplyBqsrLatest().help())
