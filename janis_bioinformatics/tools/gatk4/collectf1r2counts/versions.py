from .base import GatkCollectf1R2CountsBase


class GatkCollectf1R2Counts_4_1_3_0(GatkCollectf1R2CountsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
