from .base import Gatk4HaplotypeCallerBase
from ..gatk_latest import Gatk4Latest


class Gatk4HaplotypeCallerLatest(Gatk4Latest, Gatk4HaplotypeCallerBase):
    pass


if __name__ == "__main__":
    print(Gatk4HaplotypeCallerLatest().help())
