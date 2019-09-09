from .base import Gatk4GatherVcfsBase
from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4GatherVcfs_4_0(Gatk_4_0_12, Gatk4GatherVcfsBase):
    pass


class Gatk4GatherVcfs_4_1_3(Gatk_4_1_3_0, Gatk4GatherVcfsBase):
    pass


Gatk4GatherVcfsLatest = Gatk4GatherVcfs_4_1_3


if __name__ == "__main__":
    print(Gatk4GatherVcfs_4_0().help())
