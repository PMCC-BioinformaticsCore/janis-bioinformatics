from janis_bioinformatics.tools.illumina.manta.base import MantaBase


class Manta_1_5_0(MantaBase):
    @staticmethod
    def docker():
        return "quay.io/repository/biocontainers/manta"


MantaLatest = Manta_1_5_0
