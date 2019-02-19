from janis import Workflow, Step, Input, Output, Array, Directory
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, VcfIdx

import janis_bioinformatics.tools.gatk4 as GATK4


class ProcessBamFiles_4_0(Workflow):

    @staticmethod
    def version():
        return "4.0.12"

    def __init__(self):
        Workflow.__init__(self, "processbamfiles", friendly_name="Process BAM Files")

        inp = Input("input", Array(BamBai()))
        reference = Input("reference", FastaWithDict())
        tmpDir = Input("tmpDir", Directory())

        snps_dbsnp = Input("snps_dbsnp", VcfIdx())
        snps_1000gp = Input("snps_1000gp", VcfTabix())
        omni = Input("omni", VcfTabix())
        hapmap = Input("hapmap", VcfTabix())

        s1_merge = Step("mergeSamFiles", GATK4.Gatk4MergeSamFiles_4_0())
        s2_mark = Step("markDuplicates", GATK4.Gatk4MarkDuplicates_4_0())
        s3_recal = Step("baseRecalibrator", GATK4.Gatk4BaseRecalibrator_4_0())
        s4_bqsr = Step("applyBQSR", GATK4.Gatk4ApplyBqsr_4_0())

        # S1: MergeSamFiles
        self.add_edge(inp, s1_merge.input)
        self.add_edge(tmpDir, s1_merge.tmpDir)
        self.add_default_value(s1_merge.useThreading, True)
        self.add_default_value(s1_merge.createIndex, True)
        self.add_default_value(s1_merge.maxRecordsInRam, 5000000)
        self.add_default_value(s1_merge.validationStringency, "SILENT")

        # S2: MarkDuplicates
        self.add_edge(s1_merge, s2_mark)
        self.add_edge(tmpDir, s2_mark.tmpDir)
        self.add_default_value(s2_mark.createIndex, True)
        self.add_default_value(s2_mark.maxRecordsInRam, 5000000)

        # S3: BaseRecalibrator
        self.add_edge(s2_mark, s3_recal)
        self.add_edge(reference, s3_recal.reference)
        self.add_edge(snps_dbsnp, s3_recal.knownSites)
        self.add_edge(snps_1000gp, s3_recal.knownSites)
        self.add_edge(omni, s3_recal.knownSites)
        self.add_edge(hapmap, s3_recal.knownSites)
        self.add_edge(tmpDir, s3_recal.tmpDir)

        # S4: ApplyBQSR
        self.add_edge(s2_mark.output, s4_bqsr)
        self.add_edge(s3_recal, s4_bqsr.recalFile)
        self.add_edge(reference, s4_bqsr.reference)
        self.add_edge(tmpDir, s4_bqsr.tmpDir)

        # Outputs
        self.add_edges([
            (s4_bqsr.output, Output("output"))
        ])



if __name__ == "__main__":
    ProcessBamFiles_4_0().dump_translation("cwl")
