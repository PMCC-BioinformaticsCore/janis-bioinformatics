from ..samtools_1_7 import SamTools_1_7
from .base import SamToolsSortBase


class SamToolsSort_1_7(SamTools_1_7, SamToolsSortBase):
    pass


if __name__ == "__main__":
    print(SamToolsSort_1_7().help())
