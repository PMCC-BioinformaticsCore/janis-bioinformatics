from janis_bioinformatics.data_types import BamBai, FastaWithDict, VcfTabix, Bed
from janis_bioinformatics.tools.gatk4 import (
    Gatk4BaseRecalibrator_4_1_2,
    Gatk4ApplyBqsr_4_1_2,
)
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow


class GATKBaseRecalBQSRWorkflow_4_1_2(BioinformaticsWorkflow):
    def id(self):
        return "GATKBaseRecalBQSRWorkflow"

    def friendly_name(self):
        return "GATK Base Recalibration on Bam"

    def version(self):
        return "4.1.2"

    def tool_provider(self):
        return "common"

    def constructor(self):

        self.input("bam", BamBai)
        self.input(
            "intervals",
            Bed(optional=True),
            doc="This optional interval supports processing by regions. If this input resolves "
            "to null, then GATK will process the whole genome per each tool's spec",
        )
        self.input("reference", FastaWithDict)
        self.input("snps_dbsnp", VcfTabix)
        self.input("snps_1000gp", VcfTabix)
        self.input("known_indels", VcfTabix)
        self.input("mills_indels", VcfTabix)

        self.step(
            "base_recalibrator",
            Gatk4BaseRecalibrator_4_1_2(
                bam=self.bam,
                intervals=self.intervals,
                reference=self.reference,
                knownSites=[
                    self.snps_dbsnp,
                    self.snps_1000gp,
                    self.known_indels,
                    self.mills_indels,
                ],
            ),
        )
        self.step(
            "apply_bqsr",
            Gatk4ApplyBqsr_4_1_2(
                bam=self.bam,
                intervals=self.intervals,
                recalFile=self.base_recalibrator.out,
                reference=self.reference,
            ),
        )
        self.output("out", source=self.apply_bqsr.out)
