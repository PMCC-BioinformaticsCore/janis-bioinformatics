from janis_bioinformatics.tools.pmac.addsymtodepthofcoverage.base import (
    AddSymToDepthOfCoverageBase,
)
from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_0_7,
    PeterMacUtils_dev,
)

# NOTE: disabled as this is for dev work only
# class AddSymToDepthOfCoverage_dev(AddSymToDepthOfCoverageBase, PeterMacUtils_dev):
#     pass


class AddSymToDepthOfCoverage_0_0_7(AddSymToDepthOfCoverageBase, PeterMacUtils_0_0_7):
    pass


AddSymToDepthOfCoverageLatest = AddSymToDepthOfCoverage_0_0_7
# AddSymToDepthOfCoverageLatest = AddSymToDepthOfCoverage_dev
