from bioinformatics.janis_bioinformatics.tools import HTSLibBase


class HTSLib_1_2_1(HTSLibBase):

    @staticmethod
    def docker():
        return "biodckrdev/htslib:1.2.1"
