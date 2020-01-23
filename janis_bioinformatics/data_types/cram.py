from janis_core import File


class Cram(File):
    def __init__(self, optional=False):
        super().__init__(optional, extension=".cram")

    @staticmethod
    def name():
        return "CRAM"

    def doc(self):
        return "A binary version of a SAM file, https://samtools.github.io/hts-specs/CRAMv3.pdf"


class CramCrai(Bam):
    @staticmethod
    def name():
        return "CramPair"

    @staticmethod
    def secondary_files():
        return [".crai"]

    def doc(self):
        return "A Cram and Crai as the secondary"
