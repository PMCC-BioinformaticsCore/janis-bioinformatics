from janis_bioinformatics.tools.illumina.manta.base import MantaBase


class Manta_1_4_0(MantaBase):
    @staticmethod
    def docker():
        return "illusional/manta"


MantaLatest = Manta_1_4_0
