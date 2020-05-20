from .base import SamToolsMpileupBase
from ..samtools_1_7 import SamTools_1_7
from ..samtools_1_9 import SamTools_1_9


class SamToolsMpileup_1_7(SamTools_1_7, SamToolsMpileupBase):
    pass


class SamToolsMpileup_1_9(SamTools_1_9, SamToolsMpileupBase):
    pass


SamToolsMpileupLatest = SamToolsMpileup_1_9
