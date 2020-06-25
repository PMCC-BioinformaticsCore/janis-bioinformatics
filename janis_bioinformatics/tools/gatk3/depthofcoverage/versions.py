from .base import GATK3DepthOfCoverageBase
from ..versions import GATK3_3_8_0, GATK3_3_8_1


class GATK3DepthOfCoverage_3_8_0(GATK3_3_8_0, GATK3DepthOfCoverageBase):
    pass


class GATK3DepthOfCoverage_3_8_1(GATK3_3_8_1, GATK3DepthOfCoverageBase):
    pass


GATK3DepthOfCoverageLatest = GATK3DepthOfCoverage_3_8_1
