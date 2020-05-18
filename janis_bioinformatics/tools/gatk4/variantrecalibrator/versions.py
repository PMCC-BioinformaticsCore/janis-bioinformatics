from .base import GatkVariantrecalibratorBase


class GatkVariantrecalibrator_4_1_3_0(GatkVariantrecalibratorBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
