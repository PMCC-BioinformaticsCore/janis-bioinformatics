from .base import BedToolsIntersectBedBase
from ..bedtools_2_29_2 import BedTools_2_29_2

class BedToolsIntersectBed_2_29_2(BedTools_2_29_2,BedToolsIntersectBedBase):
    pass

BedToolsIntersectBedLatest = BedToolsIntersectBed_2_29_2
