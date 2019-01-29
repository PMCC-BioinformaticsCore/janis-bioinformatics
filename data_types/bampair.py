from janis import File
from janis.bioinformatics.data_types.bam import Bam


class BamPair(File):

    @staticmethod
    def name():
        return "BamPair"

    @staticmethod
    def secondary_files():
        return ["^.bai"]

    def doc(self):
        return "A Bam and bai as the secondary"

