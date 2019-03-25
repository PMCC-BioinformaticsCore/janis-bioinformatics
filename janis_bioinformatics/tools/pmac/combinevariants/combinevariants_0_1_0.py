from janis_bioinformatics.tools.pmac.combinevariants.base import CombineVariantsBase


class CombineVariants_0_1_0(CombineVariantsBase):
    @staticmethod
    def docker():
        return "combinevariants:0.1.0"


CombineVariantsLatest = CombineVariants_0_1_0