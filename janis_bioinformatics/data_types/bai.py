from janis_core import File


class Bai(File):
    """
    Just strictly the index file, not to be confused with a BamBai
    """

    @staticmethod
    def name():
        return "BAI"

    def doc(self):
        return "Index of the BAM file (https://www.biostars.org/p/15847/), http://software.broadinstitute.org/software/igv/bam"
