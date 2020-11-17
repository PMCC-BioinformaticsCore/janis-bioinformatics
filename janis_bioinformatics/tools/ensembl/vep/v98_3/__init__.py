from .cache import VepCacheBase_98_3
from .database import VepDatabaseBase_98_3


class Vep_98_3:
    def container(self):
        return "quay.io/biocontainers/ensembl-vep:98.3--pl526hecc5488_0"

    def version(self):
        return "98.3"


class VepCache_98_3(Vep_98_3, VepCacheBase_98_3):
    pass


class VepDatabase_98_3(Vep_98_3, VepDatabaseBase_98_3):
    pass
