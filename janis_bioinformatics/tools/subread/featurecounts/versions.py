from .base import FeatureCountsBase
from ..versions import Subread_2_0_1


class FeatureCounts_2_0_1(Subread_2_0_1, FeatureCountsBase):
    pass


FeatureCountsLatest = FeatureCounts_2_0_1
