from .base import Gatk4GatherBamFilesBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4GatherBamFiles_4_1_2(Gatk_4_1_2_0, Gatk4GatherBamFilesBase):
    pass


class Gatk4GatherBamFiles_4_1_3(Gatk_4_1_3_0, Gatk4GatherBamFilesBase):
    pass


class Gatk4GatherBamFiles_4_1_4(Gatk_4_1_4_0, Gatk4GatherBamFilesBase):
    pass


Gatk4GatherBamFilesLatest = Gatk4GatherBamFiles_4_1_4

if __name__ == "__main__":
    print(Gatk4GatherBamFilesLatest().help())
