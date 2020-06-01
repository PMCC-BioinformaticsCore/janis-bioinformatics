from .base import GatkFiltervarianttranchesBase


class GatkFiltervarianttranches_4_1_3_0(GatkFiltervarianttranchesBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
