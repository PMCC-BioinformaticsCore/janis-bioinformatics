from bioinformatics.janis_bioinformatics.tools import SamToolsLatest
from bioinformatics.janis_bioinformatics.tools import SamToolsSortBase


class SamToolsSortLatest(SamToolsLatest, SamToolsSortBase):
    pass


if __name__ == "__main__":
    print(SamToolsSortLatest().help())
