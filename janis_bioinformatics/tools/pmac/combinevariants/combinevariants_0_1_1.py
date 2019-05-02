from janis_bioinformatics.tools.pmac.combinevariants.base import CombineVariantsBase


class CombineVariants_0_1_1(CombineVariantsBase):
    @staticmethod
    def docker():
        return "michaelfranklin/combinevariants:0.1.1"


CombineVariantsLatest = CombineVariants_0_1_1