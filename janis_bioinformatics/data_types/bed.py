from janis_core import File


class Bed(File):
    def __init__(self, optional=False):
        super().__init__(optional=optional, extension=".bed")

    @staticmethod
    def name():
        return "bed"


class BedTabix(File):
    def __init__(self, optional=False):
        super().__init__(optional=optional, extension=".bed.gz")

    @staticmethod
    def name():
        return "BedTABIX"

    @staticmethod
    def secondary_files():
        return [".tbi"]
