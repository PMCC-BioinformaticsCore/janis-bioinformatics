from .base import SamToolsSortBase
from ..samtools_1_7 import SamTools_1_7
from ..samtools_1_9 import SamTools_1_9


class SamToolsSort_1_7(SamTools_1_7, SamToolsSortBase):
    pass


class SamToolsSort_1_9(SamTools_1_9, SamToolsSortBase):
    pass


SamToolsSortLatest = SamToolsSort_1_9
