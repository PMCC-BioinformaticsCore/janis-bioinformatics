from .base import GatkSplitreadsBase


class GatkSplitreads_4_1_3_0(GatkSplitreadsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
