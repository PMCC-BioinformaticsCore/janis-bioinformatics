from janis_bioinformatics.tools.pmac.extractstrelkasomaticaddp.base import (
    ExtractStrelkaSomaticADDPBase,
)

from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_0_9,
    PeterMacUtils_dev,
)


class ExtractStrelkaSomaticADDP_0_0_9(
    ExtractStrelkaSomaticADDPBase, PeterMacUtils_0_0_9
):
    pass


class ExtractStrelkaSomaticADDP_dev(ExtractStrelkaSomaticADDPBase, PeterMacUtils_dev):
    pass


ExtractStrelkaSomaticADDPLatest = ExtractStrelkaSomaticADDP_0_0_9
