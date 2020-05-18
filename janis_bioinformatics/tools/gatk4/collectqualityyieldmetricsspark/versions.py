from .base import GatkCollectqualityyieldmetricssparkBase


class GatkCollectqualityyieldmetricsspark_4_1_3_0(
    GatkCollectqualityyieldmetricssparkBase
):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
