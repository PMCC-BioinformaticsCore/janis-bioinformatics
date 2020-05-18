from .base import GatkCollectoxogmetricsBase


class GatkCollectoxogmetrics_4_1_3_0(GatkCollectoxogmetricsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
