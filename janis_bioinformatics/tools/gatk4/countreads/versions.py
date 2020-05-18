from .base import GatkCountreadsBase


class GatkCountreads_4_1_3_0(GatkCountreadsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
