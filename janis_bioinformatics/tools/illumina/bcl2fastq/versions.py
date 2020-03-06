from .base import Bcl2FastqBase
from ..illuminabase import IlluminaToolBase


class Bcl2Fastq_2_20_0(IlluminaToolBase, Bcl2FastqBase):
    def version(self):
        return "2.20.0"

    pass


Bcl2FastqLatest = Bcl2Fastq_2_20_0


if __name__ == "__main__":
    print(Bcl2FastqLatest().help())
