from janis_bioinformatics.tools.bcftools.bcftools_1_9 import BcfTools_1_9

from .base import BcfToolsConcatBase


class BcfToolsConcat_1_9(BcfTools_1_9, BcfToolsConcatBase):
    pass


BcfToolsConcatLatest = BcfToolsConcat_1_9
