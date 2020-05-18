from .base import GatkFindbreakpointevidencesparkBase


class GatkFindbreakpointevidencespark_4_1_3_0(GatkFindbreakpointevidencesparkBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
