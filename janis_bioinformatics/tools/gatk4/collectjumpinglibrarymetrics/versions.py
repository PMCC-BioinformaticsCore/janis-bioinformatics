from .base import GatkCollectjumpinglibrarymetricsBase


class GatkCollectjumpinglibrarymetrics_4_1_3_0(GatkCollectjumpinglibrarymetricsBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
