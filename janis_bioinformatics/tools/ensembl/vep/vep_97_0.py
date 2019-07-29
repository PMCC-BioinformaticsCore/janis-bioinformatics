from janis_bioinformatics.tools.ensembl.vep.basecache import VepCacheBase


class Vep_97_0:
    @staticmethod
    def container():
        return "ensemblorg/ensembl-vep:release_97.0"


class VepCache_97_0(Vep_97_0, VepCacheBase):
    pass


class VepDatabase_97_0(Vep_97_0, VepCacheBase):
    pass
