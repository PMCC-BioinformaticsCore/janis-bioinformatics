from .base import BedToolsCoverageBedBase
from ..bedtools_2_29_2 import BedTools_2_29_2


class BedToolsCoverageBed_2_29_2(BedTools_2_29_2, BedToolsCoverageBedBase):
    pass


BedToolsCoverageBedLatest = BedToolsCoverageBed_2_29_2
