from janis import Step, Input, Directory, Output
from janis_bioinformatics.tools.bcftools import BcfToolsAnnotate_1_5

from janis_bioinformatics.tools.bcftools.filter.filter_1_5 import BcfToolsFilter_1_5
from janis_bioinformatics.tools.illumina.strelka.strelka_2_9_9 import Strelka_2_9_10

from janis_bioinformatics.tools.illumina.manta.manta_1_4_0 import Manta_1_5_0

from janis_bioinformatics.tools.common import SplitMultiAllele, VarDict

from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix

from janis_bioinformatics.tools import BioinformaticsWorkflow


class VardictVariantCaller(BioinformaticsWorkflow):

    @staticmethod
    def tool_provider():
        return "PMCC"

    def __init__(self):
        super(VardictVariantCaller, self).__init__("vardictVariantCaller", "Vardict Variant Caller", doc=None)

        bam = Input("bam", BamBai())
        reference = Input("reference", FastaWithDict())

        snps_dbsnp = Input("snps_dbsnp", VcfTabix())
        snps_1000gp = Input("snps_1000gp", VcfTabix())
        omni = Input("omni", VcfTabix())
        hapmap = Input("hapmap", VcfTabix())

        vardict = VarDict()
        annotate = Step(BcfToolsAnnotate_1_5())

