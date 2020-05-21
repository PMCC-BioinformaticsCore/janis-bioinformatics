from janis_bioinformatics.tools.illumina.manta.base_cram import MantaBase


class Manta_1_4_0(MantaBase):
    def container(self):
        return "michaelfranklin/manta:1.4.0"  # add 1.4.0 after it's released

    def version(self):
        return "1.4.0"


class Manta_1_5_0(MantaBase):
    def container(self):
        return "michaelfranklin/manta:1.5.0"  # add 1.4.0 after it's released

    def version(self):
        return "1.5.0"


MantaLatest = Manta_1_5_0
