from janis import Step, Input, File, String, Float

from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import BcfToolsAnnotate_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele, VarDict


class VardictVariantCaller(BioinformaticsWorkflow):

    @staticmethod
    def tool_provider():
        return "PMCC"

    def __init__(self):
        super(VardictVariantCaller, self).__init__("vardictVariantCaller", "Vardict Variant Caller", doc=None)

        bam = Input("bam", BamBai())
        bed = Input("bed", Bed())

        sample_name = Input("sampleName", String())
        allele_freq_threshold = Input("allelFreqThreshold", Float())
        header_lines = Input("headerLines", File())

        reference = Input("reference", FastaWithDict(), "/Users/franklinmichael/reference/hg38/assembly_contigs_renamed/Homo_sapiens_assembly38.fasta")

        vardict = Step("vardict", VarDict())
        annotate = Step("annotate", BcfToolsAnnotate_1_5())
        split = Step("split", SplitMultiAllele())

        # S1: vardict
        self.add_edges([
            (bed, vardict.bed),
            (bam, vardict.bam),
            (reference, vardict.reference),
            (sample_name, vardict.sampleName),
            (sample_name, vardict.var2vcfSampleName),
            (allele_freq_threshold, vardict.alleleFreqThreshold),
            (allele_freq_threshold, vardict.var2vcfAlleleFreqThreshold)

        ])
        self.add_default_value(vardict.chromNamesAreNumbers, True)
        self.add_default_value(vardict.vcfFormat, True)
        self.add_default_value(vardict.chromColumn, 1)
        self.add_default_value(vardict.regStartCol, 2)
        self.add_default_value(vardict.geneEndCol, 3)

        # S2: annotate
        self.add_edges([
            (vardict.out, annotate),
            (header_lines, annotate.headerLines)
        ])

        # S3: split
        # S4: SplitMultiAllele
        self.add_edges([
            (reference, split.reference),
            (annotate.out, split.vcf)
        ])


if __name__ == "__main__":
    v = VardictVariantCaller()
    v.dump_translation("wdl", to_disk=True, write_inputs_file=True)
