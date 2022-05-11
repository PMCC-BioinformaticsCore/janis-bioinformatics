from .base import SamToolsViewBase
from ..samtools_1_7 import SamTools_1_7
from ..samtools_1_9 import SamTools_1_9


class SamToolsView_1_7(SamTools_1_7, SamToolsViewBase):
    pass


class SamToolsView_1_9(SamTools_1_9, SamToolsViewBase):
    pass


SamToolsViewLatest = SamToolsView_1_9
