from .base import Gatk4GenotypeConcordanceBase
from ..gatk_latest import Gatk4Latest


class Gatk4GenotypeConcordanceLatest(Gatk4Latest, Gatk4GenotypeConcordanceBase):
    pass


if __name__ == "__main__":
    print(Gatk4GenotypeConcordanceLatest().help())
