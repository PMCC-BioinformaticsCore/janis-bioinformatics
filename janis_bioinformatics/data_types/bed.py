from janis_core import File
from janis_unix.data_types import Gunzipped

from janis_bioinformatics.data_types.tabix import FileTabix


class Bed(File):
    def __init__(self, optional=False):
        super().__init__(optional=optional, extension=".bed")

    @staticmethod
    def name():
        return "bed"


class BedGz(Gunzipped):
    def __init__(self, optional=False):
        super().__init__(inner_type=Bed, optional=optional, extension=".bed.gz")

    @staticmethod
    def name():
        return "BedGz"


class BedTabix(FileTabix, BedGz):
    @staticmethod
    def name():
        return "BedTABIX"
