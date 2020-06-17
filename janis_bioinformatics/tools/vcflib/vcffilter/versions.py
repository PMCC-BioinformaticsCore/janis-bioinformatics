from ..vcflib_1_0_1 import VcfLib_1_0_1
from .base import VcfFilterBase


class VcfFilter_1_0_1(VcfLib_1_0_1, VcfFilterBase):
    pass


VcfFilterLatest = VcfFilter_1_0_1
