import os
from datetime import datetime

from janis_core.tool.test_classes import TTestCase

from janis_bioinformatics.data_types import BamBai, FastaWithDict, VcfTabix, Bed
from janis_bioinformatics.tools.gatk4 import (
    Gatk4BaseRecalibrator_4_1_3,
    Gatk4ApplyBqsr_4_1_3,
)
from janis_bioinformatics.tools.bioinformaticstoolbase import (
    BioinformaticsWorkflow,
    BioinformaticsTool,
)
from janis_core import ToolMetadata


class GATKBaseRecalBQSRWorkflow_4_1_3(BioinformaticsWorkflow):
    def id(self):
        return "GATKBaseRecalBQSRWorkflow"

    def friendly_name(self):
        return "GATK Base Recalibration on Bam"

    def version(self):
        return "4.1.3"

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
            Gatk4BaseRecalibrator_4_1_3(
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
            Gatk4ApplyBqsr_4_1_3(
                bam=self.bam,
                intervals=self.intervals,
                recalFile=self.base_recalibrator.out,
                reference=self.reference,
            ),
        )
        self.output("out", source=self.apply_bqsr.out)

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2020, 6, 12),
            dateUpdated=datetime(2020, 6, 12),
            documentation="",
        )

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "bam": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.bam",
                    ),
                    "reference": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.chr17.fasta",
                    ),
                    "snps_dbsnp": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.dbsnp138.BRCA1.vcf.gz",
                    ),
                    "snps_1000gp": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "1000G_phase1.snps.high_confidence.hg38.BRCA1.vcf.gz",
                    ),
                    "known_indels": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.known_indels.BRCA1.vcf.gz",
                    ),
                    "mills_indels": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Mills_and_1000G_gold_standard.indels.hg38.BRCA1.vcf.gz",
                    ),
                    "intervals": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "BRCA1.hg38.bed",
                    ),
                },
                output=BamBai.basic_test(
                    "out",
                    2600000,
                    21000,
                    os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.recalibrated.flagstat",
                    ),
                ),
            )
        ]
