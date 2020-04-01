from .base import BedToolsGenomeCoverageBedBase
from ..bedtools_2_29_2 import BedTools_2_29_2


class BedToolsGenomeCoverageBed_2_29_2(BedTools_2_29_2, BedToolsGenomeCoverageBedBase):
    pass


BedToolsGenomeCoverageBedLatest = BedToolsGenomeCoverageBed_2_29_2
