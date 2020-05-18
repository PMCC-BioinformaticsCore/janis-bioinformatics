from .base import GatkGenomicsdbimportBase


class GatkGenomicsdbimport_4_1_3_0(GatkGenomicsdbimportBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
