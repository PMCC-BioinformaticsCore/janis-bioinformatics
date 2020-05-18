from .base import GatkFuncotatorBase


class GatkFuncotator_4_1_3_0(GatkFuncotatorBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
