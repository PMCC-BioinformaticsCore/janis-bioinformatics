from janis_core import Step, Input, Output, Array, String

from janis_bioinformatics.data_types import FastaWithDict, BamBai, BedTabix
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import BcfToolsView_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele
from janis_bioinformatics.tools.illumina import (
    StrelkaGermline_2_9_10,
    Manta_1_5_0,
    StrelkaSomatic_2_9_10,
)


class IlluminaSomaticVariantCaller(BioinformaticsWorkflow):
    @staticmethod
    def tool_provider():
        return "Variant Callers"

    @staticmethod
    def version():
        return "v0.1.0"

    def __init__(self):
        super(IlluminaSomaticVariantCaller, self).__init__(
            "strelkaSomaticVariantCaller", "Strelka Somatic Variant Caller", doc=None
        )

        normal = Input("normalBam", BamBai())
        tumor = Input("tumorBam", BamBai())

        reference = Input("reference", FastaWithDict())
        intervals = Input("intervals", BedTabix(optional=True))

        manta = Step("manta", Manta_1_5_0())
        strelka = Step("strelka", StrelkaSomatic_2_9_10())
        bcf_view = Step("bcf_view", BcfToolsView_1_5())
        split = Step("splitMultiAllele", SplitMultiAllele())

        # S1: Manta
        self.add_edges(
            [
                (normal, manta.bam),
                (tumor, manta.tumorBam),
                (reference, manta.reference),
                (intervals, manta.callRegions),
            ]
        )

        # S2: Strelka
        self.add_edges(
            [
                (normal, strelka.normalBam),
                (tumor, strelka.tumorBam),
                (reference, strelka.reference),
                (manta.candidateSmallIndels, strelka.indelCandidates),
                (intervals, strelka.callRegions),
            ]
        )

        # S3: BcfTools Filter
        self.add_edge(strelka.snvs, bcf_view.file)
        self.add_edge(
            Input("filters", Array(String()), default=["PASS"]), bcf_view.applyFilters
        )

        # S4: SplitMultiAllele
        self.add_edges([(reference, split.reference), (bcf_view.out, split.vcf)])

        ## Outputs
        self.add_edges(
            [
                (manta.diploidSV, Output("diploid")),
                (strelka.snvs, Output("variants")),
                (split.out, Output("out")),
            ]
        )


if __name__ == "__main__":

    wf = IlluminaSomaticVariantCaller()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
