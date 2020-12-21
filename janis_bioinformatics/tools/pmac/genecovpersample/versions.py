from janis_bioinformatics.tools.pmac.genecovpersample.base import (
    GeneCoveragePerSampleBase,
)
from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_0_7,
    PeterMacUtils_0_0_8,
    PeterMacUtils_dev,
)


class GeneCoveragePerSample_0_0_7(GeneCoveragePerSampleBase, PeterMacUtils_0_0_7):
    pass


class GeneCoveragePerSample_0_0_8(GeneCoveragePerSampleBase, PeterMacUtils_0_0_8):
    pass


# NOTE: disabled as this is for dev work only
# class GeneCoveragePerSample_dev(GeneCoveragePerSampleBase, PeterMacUtils_dev):
#     pass


GeneCoveragePerSampleLatest = GeneCoveragePerSample_0_0_8
# GeneCoveragePerSampleLatest = GeneCoveragePerSample_dev
