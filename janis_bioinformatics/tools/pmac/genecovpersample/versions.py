from janis_bioinformatics.tools.pmac.genecovpersample.base import (
    GeneCoveragePerSampleBase,
)
from janis_bioinformatics.tools.pmac.versions import PeterMacUtils_dev


class GeneCoveragePerSample_dev(GeneCoveragePerSampleBase, PeterMacUtils_dev):
    pass


GeneCoveragePerSampleLatest = GeneCoveragePerSample_dev
