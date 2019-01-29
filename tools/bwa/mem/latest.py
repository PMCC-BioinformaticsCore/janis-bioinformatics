from janis.bioinformatics.tools.bwa.bwalatest import BwaLatest
from janis.bioinformatics.tools.bwa.mem.membase import BwaMemBase


class BwaMemLatest(BwaLatest, BwaMemBase):
    pass


if __name__ == "__main__":
    print(BwaMemLatest().help())
