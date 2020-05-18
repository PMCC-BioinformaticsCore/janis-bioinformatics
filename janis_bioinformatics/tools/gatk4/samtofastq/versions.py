from .base import GatkSamtofastqBase


class GatkSamtofastq_4_1_3_0(GatkSamtofastqBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
