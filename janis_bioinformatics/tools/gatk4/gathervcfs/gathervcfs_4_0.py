from .base import Gatk4GatherVcfsBase
from ..gatk_4_0_12 import Gatk_4_0_12


class Gatk4GatherVcfs_4_0(Gatk_4_0_12, Gatk4GatherVcfsBase):
    pass


if __name__ == "__main__":
    print(Gatk4GatherVcfs_4_0().help())
