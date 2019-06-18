from janis import File


class Bed(File):
    @staticmethod
    def name():
        return "bed"


class BedTabix(File):
    @staticmethod
    def name():
        return "BedTABIX"

    @staticmethod
    def secondary_files():
        return [".tbi"]
