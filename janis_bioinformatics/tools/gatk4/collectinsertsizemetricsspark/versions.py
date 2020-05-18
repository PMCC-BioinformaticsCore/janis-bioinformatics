from .base import GatkCollectinsertsizemetricssparkBase


class GatkCollectinsertsizemetricsspark_4_1_3_0(GatkCollectinsertsizemetricssparkBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
