from .base import GatkCollectalleliccountsBase


class GatkCollectalleliccounts_4_1_3_0(GatkCollectalleliccountsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
