from janis_bioinformatics.tools.pmac.extractstrelkasomaticaddp.base import (
    ExtractStrelkaSomaticADDPBase,
)

from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_1_1,
    PeterMacUtils_dev,
)


class ExtractStrelkaSomaticADDP_0_1_1(
    ExtractStrelkaSomaticADDPBase, PeterMacUtils_0_1_1
):
    pass


class ExtractStrelkaSomaticADDP_dev(ExtractStrelkaSomaticADDPBase, PeterMacUtils_dev):
    pass


ExtractStrelkaSomaticADDPLatest = ExtractStrelkaSomaticADDP_0_1_1
