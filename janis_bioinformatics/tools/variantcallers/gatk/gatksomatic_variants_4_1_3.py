import os
from datetime import date

from janis_core import String, Array, WorkflowBuilder
from janis_core.tool.test_classes import TTestCase
from janis_unix.tools import UncompressArchive
from janis_bioinformatics.tools import gatk4, BioinformaticsTool
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed, Vcf
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAllele
from janis_bioinformatics.tools.htslib import BGZipLatest, TabixLatest
from janis_bioinformatics.tools.vcftools import VcfToolsvcftoolsLatest


class GatkSomaticVariantCaller_4_1_3(BioinformaticsWorkflow):
    def id(self):
        return "GATK4_SomaticVariantCaller"

    def friendly_name(self):
        return "GATK4 Somatic Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def constructor(self):

        self.input("normal_bam", BamBai)
        self.input("tumor_bam", BamBai)
        self.input("normal_name", String(optional=True))
        self.input(
            "intervals",
            Bed(optional=True),
            doc="This optional intervals file supports processing by regions. If this file resolves "
            "to null, then GATK will process the whole genome per each tool's spec",
        )
        self.input("reference", FastaWithDict)
        self.input("gnomad", VcfTabix)
        self.input("panel_of_normals", VcfTabix(optional=True))
        self.input("output_bam_name", String(optional=True))

        # split normal and tumor bam
        self.step(
            "normal_split_bam",
            self.process_subpipeline(bam=self.normal_bam, intervals=self.intervals),
        )
        self.step(
            "tumor_split_bam",
            self.process_subpipeline(bam=self.tumor_bam, intervals=self.intervals),
        )

        # variant calling + learn read orientation model
        self.step(
            "mutect2",
            gatk4.GatkMutect2_4_1_3(
                normalBams=[self.normal_split_bam.out],
                tumorBams=[self.tumor_split_bam.out],
                normalSample=self.normal_name,
                intervals=self.intervals,
                reference=self.reference,
                germlineResource=self.gnomad,
                panelOfNormals=self.panel_of_normals,
                outputPrefix=self.normal_name,
                outputBamName=self.output_bam_name,
            ),
        )
        self.step(
            "learnorientationmodel",
            gatk4.Gatk4LearnReadOrientationModelLatest(
                f1r2CountsFiles=self.mutect2.f1f2r_out,
            ),
        )

        # calculate contamination and segmentation
        self.step(
            "getpileupsummaries",
            gatk4.Gatk4GetPileUpSummariesLatest(
                bam=self.tumor_split_bam.out,
                sites=self.gnomad,
                intervals=self.intervals,
            ),
        )
        self.step(
            "calculatecontamination",
            gatk4.Gatk4CalculateContaminationLatest(
                pileupTable=self.getpileupsummaries.out,
            ),
        )
        self.step(
            "filtermutect2calls",
            gatk4.Gatk4FilterMutectCallsLatest(
                vcf=self.mutect2.out,
                reference=self.reference,
                segmentationFile=self.calculatecontamination.segOut,
                contaminationTable=self.calculatecontamination.contOut,
                readOrientationModel=self.learnorientationmodel.out,
                statsFile=self.mutect2.stats,
            ),
        )

        # normalise and filter "PASS" variants
        self.step("uncompressvcf", UncompressArchive(file=self.filtermutect2calls.out))
        self.step(
            "splitnormalisevcf",
            SplitMultiAllele(
                vcf=self.uncompressvcf.out.as_type(Vcf), reference=self.reference
            ),
        )
        self.step(
            "filterpass",
            VcfToolsvcftoolsLatest(
                vcf=self.splitnormalisevcf.out,
                removeFileteredAll=True,
                recode=True,
                recodeINFOAll=True,
            ),
        )

        self.output("variants", source=self.filtermutect2calls.out)
        self.output("out_bam", source=self.mutect2.bam)
        self.output("out", source=self.filterpass.out)

    @staticmethod
    def process_subpipeline(**connections):
        w = WorkflowBuilder("split_bam_subpipeline")

        w.input("bam", BamBai)
        w.input("intervals", Bed(optional=True))
        w.step(
            "split_bam", gatk4.Gatk4SplitReads_4_1_3(bam=w.bam, intervals=w.intervals)
        )
        w.output("out", source=w.split_bam.out)

        return w(**connections)

    def bind_metadata(self):
        self.metadata.version = "4.1.3.0"
        self.metadata.dateCreated = date(2019, 2, 1)
        self.metadata.dateUpdated = date(2020, 6, 15)

        self.metadata.contributors = ["Michael Franklin", "Jiaan Yu"]
        self.metadata.keywords = [
            "variants",
            "gatk",
            "gatk4",
            "variant caller",
            "somatic",
            "paired",
        ]
        self.metadata.documentation = """
        This is a VariantCaller based on the GATK Best Practice pipelines. It uses the GATK4 toolkit, specifically 4.0.12.0. Takes GATK Base Recalibrated Bam as input

        It has the following steps:

        1. Mutect2
        2. LearnOrientationModel
        3. GetPileUpSummaries
        4. CalculateContamination
        5. FilterMutectCalls
        6. Split and normliase vcf
        7. Filter PASS variants
                """.strip()

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "normal_bam": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgssomatic_data",
                        "NA24385-BRCA1.markduped.recalibrated.bam",
                    ),
                    "tumor_bam": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgssomatic_data",
                        "NA12878-NA24385-mixture.markduped.recalibrated.bam",
                    ),
                    "reference": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.chr17.fasta",
                    ),
                    "gnomad": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgssomatic_data",
                        "af-only-gnomad.hg38.BRCA1.vcf.gz",
                    ),
                    "normal_name": "NA24385-BRCA1",
                    "intervals": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "BRCA1.hg38.bed",
                    ),
                    "filterpass_removeFileteredAll": True,
                    "filterpass_recode": True,
                    "filterpass_recodeINFOAll": True,
                    "output_bam_name": "mutect2.bam",
                },
                output=Vcf.basic_test(
                    "out",
                    33000,
                    147,
                    ["GATKCommandLine"],
                    "c083775bc8c49397fb65ec12cd435688",
                )
                + VcfTabix.basic_test(
                    "variants",
                    13000,
                    260,
                    182,
                    ["GATKCommandLine"],
                    "6cfd70dda8599a270978868166ab6545",
                )
                + BamBai.basic_test(
                    "out_bam",
                    813200,
                    21200,
                    os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgssomatic_data",
                        "somatic_variant_caller.flagstat",
                    ),
                ),
            ),
        ]


if __name__ == "__main__":
    vc = GatkSomaticVariantCaller_4_1_3().translate("wdl", to_console=True)
    # print(vc.translate("cwl"))
