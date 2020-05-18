from .base import GatkUnmarkduplicatesBase


class GatkUnmarkduplicates_4_1_3_0(GatkUnmarkduplicatesBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
