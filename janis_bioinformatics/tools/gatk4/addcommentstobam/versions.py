from .base import GatkAddcommentstobamBase


class GatkAddcommentstobam_4_1_3_0(GatkAddcommentstobamBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
