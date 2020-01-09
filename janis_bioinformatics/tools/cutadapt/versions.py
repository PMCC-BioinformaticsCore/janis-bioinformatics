from janis_bioinformatics.tools.cutadapt.base_1 import CutAdaptBase_1

from janis_bioinformatics.tools.cutadapt.base_2 import CutAdaptBase_2


class CutAdapt_1_18(CutAdaptBase_1):
    def container(self):
        return "quay.io/biocontainers/cutadapt:1.18--py37h14c3975_1"

    def version(self):
        return "1.18"


class CutAdapt_2_4(CutAdaptBase_2):
    def container(self):
        return "quay.io/biocontainers/cutadapt:2.4--py37h14c3975_0"

    def version(self):
        return "2.4"


class CutAdapt_2_5(CutAdaptBase_2):
    def container(self):
        return "quay.io/biocontainers/cutadapt:2.5--py37h516909a_0"

    def version(self):
        return "2.5"


class CutAdapt_2_6(CutAdaptBase_2):
    def container(self):
        return "quay.io/biocontainers/cutadapt:2.6--py36h516909a_0"

    def version(self):
        return "2.6"


CutAdaptLatest = CutAdapt_2_6


CutAdaptLatest().wrapped_in_wf().translate(
    "wdl", to_console=False, to_disk=True, validate=True
)
