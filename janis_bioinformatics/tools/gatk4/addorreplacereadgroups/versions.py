from .base import Gatk4AddOrReplaceReadGroupsBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4AddOrReplaceReadGroups_4_0(Gatk_4_0_12, Gatk4AddOrReplaceReadGroupsBase):
    pass


class Gatk4AddOrReplaceReadGroups_4_1_2(Gatk_4_1_2_0, Gatk4AddOrReplaceReadGroupsBase):
    pass


class Gatk4AddOrReplaceReadGroups_4_1_3(Gatk_4_1_3_0, Gatk4AddOrReplaceReadGroupsBase):
    pass


class Gatk4AddOrReplaceReadGroups_4_1_4(Gatk_4_1_4_0, Gatk4AddOrReplaceReadGroupsBase):
    pass


Gatk4AddOrReplaceReadGroupsLatest = Gatk4AddOrReplaceReadGroups_4_1_4
