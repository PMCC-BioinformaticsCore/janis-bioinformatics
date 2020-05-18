from .base import GatkMarkilluminaadaptersBase


class GatkMarkilluminaadapters_4_1_3_0(GatkMarkilluminaadaptersBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
