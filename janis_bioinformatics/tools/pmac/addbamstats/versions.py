from janis_bioinformatics.tools.pmac.addbamstats.base import AddBamStatsBase
from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_0_7,
    PeterMacUtils_dev,
)

# NOTE: disabled as this is for dev work only
# class AddBamStats_dev(AddBamStatsBase, PeterMacUtils_dev):
#     pass


class AddBamStats_0_0_7(AddBamStatsBase, PeterMacUtils_0_0_7):
    pass


AddBamStatsLatest = AddBamStats_0_0_7
