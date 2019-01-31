from janis import File


class Bam(File):

    @staticmethod
    def name():
        return "BAM"

    def doc(self):
        return "A binary version of a SAM file, http://software.broadinstitute.org/software/igv/bam"


class BamBai(File):

    @staticmethod
    def name():
        return "BamPair"

    @staticmethod
    def secondary_files():
        return ["^.bai"]

    def doc(self):
        return "A Bam and bai as the secondary"

