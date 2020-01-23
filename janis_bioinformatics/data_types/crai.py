from janis_core import File


class Crai(File):
    """
    Just strictly the index file, not to be confused with a CramCrai
    """

    @staticmethod
    def name():
        return "CRAI"

    def doc(self):
        return "Index of the CRAM file https://samtools.github.io/hts-specs/CRAMv3.pdf"
