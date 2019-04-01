from janis import Step, Input, Directory, Output

from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import BcfToolsView_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele
from janis_bioinformatics.tools.illumina.manta.manta_1_4_0 import Manta_1_5_0
from janis_bioinformatics.tools.illumina.strelka.strelka_2_9_9 import Strelka_2_9_10


class StrelkaVariantCaller(BioinformaticsWorkflow):

    @staticmethod
    def tool_provider():
        return "Illumina"

    def __init__(self):
        super(StrelkaVariantCaller, self).__init__("strelkaVariantCaller", "Strelka Variant Caller", doc=None)

        bam = Input("bam", BamBai())
        reference = Input("reference", FastaWithDict())

        manta = Step("manta", Manta_1_5_0())
        strelka = Step("strelka", Strelka_2_9_10())
        bcf_view = Step("bcf_view", BcfToolsView_1_5())
        split = Step("splitMultiAllele", SplitMultiAllele())


        # S1: Manta
        self.add_edges([
            (bam, manta.bam),
            (reference, manta.reference),
        ])

        # S2: Strelka
        self.add_edges([
            (bam, strelka.bam),
            (reference, strelka.reference),
            (manta.candidateSmallIndels, strelka.indelCandidates),
        ])

        # S3: BcfTools Filter
        self.add_edge(strelka.variants, bcf_view.file)
        self.add_default_value(bcf_view.applyFilters, ["PASS"])


        # S4: SplitMultiAllele
        self.add_edges([
            (reference, split.reference),
            (bcf_view.out, split.vcf),
            (split.out, Output("splitOut"))

        ])

        ## Outputs
        self.add_edges([
            (manta.diploidSV, Output("diploid")),
            (strelka.variants, Output("variants")),
            (split.out, Output("out"))
        ])


if __name__ == "__main__":

    wf = StrelkaVariantCaller()
    wdl = wf.dump_translation("wdl", to_console=True, to_disk=False, write_inputs_file=False)
