from janis_bioinformatics.tools.pmac.combinevariants.base import CombineVariantsBase
from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_0_4,
    PeterMacUtils_0_0_5,
)


class CombineVariants_0_0_4(CombineVariantsBase, PeterMacUtils_0_0_4):
    pass


class CombineVariants_0_0_5(CombineVariantsBase, PeterMacUtils_0_0_5):
    pass


CombineVariantsLatest = CombineVariants_0_0_5
