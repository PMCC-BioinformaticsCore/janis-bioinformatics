from .base import Gatk4HaplotypeCallerBase
from ..gatk_4_0 import Gatk_4_0


class Gatk4HaplotypeCaller_4_0(Gatk_4_0, Gatk4HaplotypeCallerBase):
    pass


if __name__ == "__main__":
    print(Gatk4HaplotypeCaller_4_0().help())
