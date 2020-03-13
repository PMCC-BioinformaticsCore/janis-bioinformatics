from .base import Bcl2FastqBase


class Bcl2Fastq_2_20_0(Bcl2FastqBase):
    def container(self):
        return None

    def version(self):
        return "2.20.0"

    pass


Bcl2FastqLatest = Bcl2Fastq_2_20_0


if __name__ == "__main__":
    print(Bcl2FastqLatest().help())
