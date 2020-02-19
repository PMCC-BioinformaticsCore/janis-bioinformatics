from .base import SamToolsFaidxBase

from janis_bioinformatics.tools.samtools.samtools_1_7 import SamTools_1_7
from janis_bioinformatics.tools.samtools.samtools_1_9 import SamTools_1_9


class SamToolsFaidx_1_7(SamTools_1_7, SamToolsFaidxBase):
    pass


class SamToolsFaidx_1_9(SamTools_1_9, SamToolsFaidxBase):
    pass


SamToolsFaidxLatest = SamToolsFaidx_1_9
