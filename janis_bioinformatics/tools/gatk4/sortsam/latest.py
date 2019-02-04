from .base import Gatk4SortSamBase
from ..gatk_latest import Gatk4Latest


class Gatk4SortSamLatest(Gatk4Latest, Gatk4SortSamBase):
    pass


if __name__ == "__main__":
    print(Gatk4SortSamLatest().help())
