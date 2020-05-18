from .base import GatkAnalyzesaturationmutagenesisBase


class GatkAnalyzesaturationmutagenesis_4_1_3_0(GatkAnalyzesaturationmutagenesisBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
