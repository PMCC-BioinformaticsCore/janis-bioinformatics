from .base import Gatk4PrintReadsBase
from ..gatk_latest import Gatk4Latest


class Gatk4PrintReadsLatest(Gatk4Latest, Gatk4PrintReadsBase):
    pass


if __name__ == "__main__":
    print(Gatk4PrintReadsLatest().help())
