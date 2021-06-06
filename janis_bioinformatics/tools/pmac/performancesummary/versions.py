from janis_bioinformatics.tools.pmac.performancesummary.base import (
    PerformanceSummaryBase,
)
from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_0_7,
    PeterMacUtils_dev,
)


class PerformanceSummary_0_0_7(PerformanceSummaryBase, PeterMacUtils_0_0_7):
    pass


# NOTE: disabled as this is for dev work only
# class PerformanceSummary_dev(PerformanceSummaryBase, PeterMacUtils_dev):
#     pass


PerformanceSummaryLatest = PerformanceSummary_0_0_7
# PerformanceSummaryLatest = PerformanceSummary_dev
