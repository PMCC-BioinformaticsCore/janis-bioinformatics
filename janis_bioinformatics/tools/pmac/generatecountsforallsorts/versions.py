from janis_bioinformatics.tools.pmac.generatecountsforallsorts.base import (
    GenerateCountsForALLSortsBase,
)

from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_1_2,
    PeterMacUtils_dev,
)


class GenerateCountsForALLSorts_0_1_0(
    GenerateCountsForALLSortsBase, PeterMacUtils_0_1_2
):
    pass


GenerateCountsForALLSortsLatest = GenerateCountsForALLSorts_0_1_0
