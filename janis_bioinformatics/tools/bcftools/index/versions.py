from janis_bioinformatics.tools.bcftools.bcftools_1_9 import BcfTools_1_9

from .base import BcfToolsIndexBase


class BcfToolsIndex_1_9(BcfTools_1_9, BcfToolsIndexBase):
    pass


BcfToolsIndexLatest = BcfToolsIndex_1_9
