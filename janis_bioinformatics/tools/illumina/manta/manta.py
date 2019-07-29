from janis_bioinformatics.tools.illumina.manta.base import MantaBase


class Manta_1_4_0(MantaBase):
    @staticmethod
    def container():
        return "michaelfranklin/manta:1.4.0"  # add 1.4.0 after it's released

    @staticmethod
    def version():
        return "1.4.0"


class Manta_1_5_0(MantaBase):
    @staticmethod
    def container():
        return "michaelfranklin/manta:1.5.0"  # add 1.4.0 after it's released

    @staticmethod
    def version():
        return "1.5.0"


MantaLatest = Manta_1_5_0
