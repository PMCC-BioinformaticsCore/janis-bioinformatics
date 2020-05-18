from .base import GatkFixvcfheaderBase


class GatkFixvcfheader_4_1_3_0(GatkFixvcfheaderBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
