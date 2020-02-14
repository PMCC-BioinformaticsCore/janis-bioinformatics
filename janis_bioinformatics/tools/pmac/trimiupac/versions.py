from janis_bioinformatics.tools.pmac.trimiupac.base import TrimIUPACBase
from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_0_4,
    PeterMacUtils_0_0_5,
)


class TrimIUPAC_0_0_4(TrimIUPACBase, PeterMacUtils_0_0_4):
    pass


class TrimIUPAC_0_0_5(TrimIUPACBase, PeterMacUtils_0_0_5):
    pass


TrimIUPACLatest = TrimIUPAC_0_0_5
