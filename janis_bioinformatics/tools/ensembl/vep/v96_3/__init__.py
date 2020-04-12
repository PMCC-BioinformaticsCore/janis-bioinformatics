from .basecache import VepCacheBase_96_3
from .basedatabase import VepDatabaseBase_96_3


class Vep_96_3:
    def container(self):
        return "ensemblorg/ensembl-vep:release_96.3"

    def version(self):
        return "96.3"


class VepCache_96_3(Vep_96_3, VepCacheBase_96_3):
    pass


class VepDatabase_96_3(Vep_96_3, VepDatabaseBase_96_3):
    pass
