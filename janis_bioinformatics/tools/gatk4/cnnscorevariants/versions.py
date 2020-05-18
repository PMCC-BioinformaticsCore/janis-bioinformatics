from .base import GatkCnnscorevariantsBase


class GatkCnnscorevariants_4_1_3_0(GatkCnnscorevariantsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
