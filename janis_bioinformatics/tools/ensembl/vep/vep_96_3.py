from janis_bioinformatics.tools.ensembl.vep.basecache import VepCacheBase


class Vep_96_3:
    @staticmethod
    def container():
        return "ensemblorg/ensembl-vep:release_96.3"


class VepCache_96_3(Vep_96_3, VepCacheBase):
    pass


class VepDatabase_96_3(Vep_96_3, VepCacheBase):
    pass
