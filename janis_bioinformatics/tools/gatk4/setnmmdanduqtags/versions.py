from janis_bioinformatics.tools.gatk4 import Gatk_4_1_3_0, Gatk_4_1_4_0

from .base import Gatk4SetNmMdAndUqTagsBase


class Gatk4SetNmMdAndUqTags_4_1_3(Gatk_4_1_3_0, Gatk4SetNmMdAndUqTagsBase):
    pass


class Gatk4SetNmMdAndUqTags_4_1_4(Gatk_4_1_4_0, Gatk4SetNmMdAndUqTagsBase):
    pass


Gatk4SetNmMdAndUqTagsLatest = Gatk4SetNmMdAndUqTags_4_1_4
