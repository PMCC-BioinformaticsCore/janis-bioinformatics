from janis_bioinformatics.tools.illumina.manta.base import MantaBase


class Manta_1_4_0(MantaBase):
    @staticmethod
    def docker():
        return "illusional/manta"  # add 1.4.0 after it's released

    @staticmethod
    def version():
        return "1.4.0"


MantaLatest = Manta_1_4_0
