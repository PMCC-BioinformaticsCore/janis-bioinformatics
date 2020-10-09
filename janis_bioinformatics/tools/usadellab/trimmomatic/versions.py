from .base_singleend import TrimmomaticSingleEndBase
from .base_pairedend import TrimmomaticPairedEndBase


class Trimmomatic_0_35:
    def container(self):
        return "quay.io/biocontainers/trimmomatic:0.35--6"

    def version(self):
        return "0.35"


class TrimmomaticSingleEnd_0_35(Trimmomatic_0_35, TrimmomaticSingleEndBase):
    pass


class TrimmomaticPairedEnd_0_35(Trimmomatic_0_35, TrimmomaticPairedEndBase):
    pass


TrimmomaticSingleEndLatest = TrimmomaticSingleEnd_0_35
TrimmomaticPairedEndLatest = TrimmomaticPairedEnd_0_35
