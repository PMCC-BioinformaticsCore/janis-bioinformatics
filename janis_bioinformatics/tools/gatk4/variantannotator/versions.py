from .base import GatkVariantannotatorBase


class GatkVariantannotator_4_1_3_0(GatkVariantannotatorBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
