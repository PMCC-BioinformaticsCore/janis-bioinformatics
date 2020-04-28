from .base import SamToolsFlagstatBase
from ..samtools_1_7 import SamTools_1_7
from ..samtools_1_9 import SamTools_1_9


class SamToolsFlagstat_1_7(SamTools_1_7, SamToolsFlagstatBase):
    pass


class SamToolsFlagstat_1_9(SamTools_1_9, SamToolsFlagstatBase):
    pass


SamToolsFlagstatLatest = SamToolsFlagstat_1_9
