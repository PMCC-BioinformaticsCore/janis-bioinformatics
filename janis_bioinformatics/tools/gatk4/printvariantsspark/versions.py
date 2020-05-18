from .base import GatkPrintvariantssparkBase


class GatkPrintvariantsspark_4_1_3_0(GatkPrintvariantssparkBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
