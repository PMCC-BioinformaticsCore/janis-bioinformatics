from .base import GatkValidatesamfileBase


class GatkValidatesamfile_4_1_3_0(GatkValidatesamfileBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
