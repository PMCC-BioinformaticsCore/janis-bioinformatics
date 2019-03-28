from janis import Step, Input, Directory, Output

from janis_bioinformatics.tools.bcftools.filter.filter_1_5 import BcfToolsFilter_1_5
from janis_bioinformatics.tools.illumina.strelka.strelka_2_9_9 import Strelka_2_9_10

from janis_bioinformatics.tools.illumina.manta.manta_1_4_0 import Manta_1_5_0

from janis_bioinformatics.tools.common import SplitMultiAllele

from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix

from janis_bioinformatics.tools import BioinformaticsWorkflow


class StrelkaVariantCaller(BioinformaticsWorkflow):

    @staticmethod
    def tool_provider():
        return "Illumina"

    def __init__(self):
        super(StrelkaVariantCaller, self).__init__("strelkaVariantCaller", "Strelka Variant Caller", doc=None)

        bam = Input("bam", BamBai())
        reference = Input("reference", FastaWithDict())

        snps_dbsnp = Input("snps_dbsnp", VcfTabix())
        snps_1000gp = Input("snps_1000gp", VcfTabix())
        omni = Input("omni", VcfTabix())
        hapmap = Input("hapmap", VcfTabix())

        tmpDir = Input("tmpDir", Directory())


        manta = Step("manta", Manta_1_5_0())
        strelka = Step("strelka", Strelka_2_9_10())
        bcftools_fp = Step("bcftools_filerpass", BcfToolsFilter_1_5())
        split = Step("splitMultiAllele", SplitMultiAllele())


        # S1: Manta
        self.add_edges([
            (bam, manta.bam),
            (reference, manta.reference),
        ])

        # S2: Strelka
        self.add_edges([
            (bam, strelka),
            (reference, strelka),
            (manta.candidateSmallIndels, strelka.indelCandidates),
        ])

        # S3: BcfTools Filter
        self.add_edges([

        ])


        # S4: SplitMultiAllele
        self.add_edges([
            (reference, split.reference),
            (bcftools_fp, split.input),
        ])


        ## Outputs
        self.add_edges([
            (manta.diploidSV, Output("diploid")),
            (strelka.variants, Output("variants")),
            (split.out, Output("out"))
        ])
