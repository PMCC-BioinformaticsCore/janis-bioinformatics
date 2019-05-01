from .base import Gatk4GatherVcfsBase
from ..gatk_4_0 import Gatk_4_0


class Gatk4GatherVcfs_4_0(Gatk_4_0, Gatk4GatherVcfsBase):
    pass


if __name__ == "__main__":
    print(Gatk4GatherVcfs_4_0().help())
