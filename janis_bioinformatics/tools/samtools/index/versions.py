from .base import SamToolsIndexBase
from janis_bioinformatics.tools.samtools.samtools_1_9 import SamTools_1_9

from janis_bioinformatics.tools.samtools.samtools_1_7 import SamTools_1_7


class SamToolsIndex_1_7(SamTools_1_7, SamToolsIndexBase):
    pass


class SamToolsIndex_1_9(SamTools_1_9, SamToolsIndexBase):
    pass


SamToolsIndexLatest = SamToolsIndex_1_9
