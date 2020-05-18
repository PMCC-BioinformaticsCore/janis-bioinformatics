from .base import GatkVcfformatconverterBase


class GatkVcfformatconverter_4_1_3_0(GatkVcfformatconverterBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
