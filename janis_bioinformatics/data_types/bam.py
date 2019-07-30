from janis_core import File


class Bam(File):
    def __init__(self, optional=False):
        super().__init__(optional, extension=".bam")

    @staticmethod
    def name():
        return "BAM"

    def doc(self):
        return "A binary version of a SAM file, http://software.broadinstitute.org/software/igv/bam"


class BamBai(Bam):
    @staticmethod
    def name():
        return "BamPair"

    @staticmethod
    def secondary_files():
        return ["^.bai"]

    def doc(self):
        return "A Bam and bai as the secondary"
