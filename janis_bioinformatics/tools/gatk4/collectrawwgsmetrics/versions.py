from .base import GatkCollectrawwgsmetricsBase


class GatkCollectrawwgsmetrics_4_1_3_0(GatkCollectrawwgsmetricsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
