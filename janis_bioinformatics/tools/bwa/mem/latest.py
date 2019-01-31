from bioinformatics.janis_bioinformatics.tools import BwaLatest
from bioinformatics.janis_bioinformatics.tools import BwaMemBase


class BwaMemLatest(BwaLatest, BwaMemBase):
    pass


if __name__ == "__main__":
    print(BwaMemLatest().help())
