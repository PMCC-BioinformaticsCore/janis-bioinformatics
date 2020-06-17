from datetime import date

from janis_core import String, WorkflowBuilder, Array
from janis_bioinformatics.tools import gatk4
from janis_bioinformatics.tools.common import SplitMultiAlleleNormaliseVcf
from janis_bioinformatics.tools.vcftools import VcfToolsvcftoolsLatest
from janis_bioinformatics.tools.pmac import AddBamStatsSomatic_0_1_0
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow


class GatkSomaticVariantCallerTumorOnlyTargeted(BioinformaticsWorkflow):
    def id(self):
        return "GATK4_SomaticVariantCallerTumorOnlyTargeted"

    def friendly_name(self):
        return "GATK4 Somatic Variant Caller for Tumour Only Samples with Targeted BED"

    def tool_provider(self):
        return "Variant Callers"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        self.metadata.version = "4.1.3.0"
        self.metadata.dateCreated = date(2020, 6, 4)
        self.metadata.dateUpdated = date(2020, 6, 4)

        self.metadata.contributors = ["Michael Franklin", "Jiaan Yu"]
        self.metadata.keywords = ["variants", "gatk", "gatk4", "variant caller"]
        self.metadata.documentation = """
        This is a VariantCaller based on the GATK Best Practice pipelines. It uses the GATK4 toolkit, specifically 4.1.3.

        It has the following steps:

        1. Mutect2 (output: vcf, bam, f1r2.tar.gz)
        2. LearnOrientationModel
        3. GetPileupSummaries
        4. CalculateContamination
        5. FilterMutect2Calls
        6. SplitNormaliseVcf
                """.strip()

    def constructor(self):

        self.input("bam", BamBai)
        self.input(
            "intervals",
            Bed(optional=True),
            doc="This optional interval supports processing by regions. If this input resolves "
            "to null, then GATK will process the whole genome per each tool's spec",
        )
        self.input("reference", FastaWithDict)
        self.input("gnomad", VcfTabix)
        self.input("panel_of_normals", VcfTabix(optional=True))

        # variant calling + learn read orientation model
        self.step(
            "mutect2",
            gatk4.GatkMutect2_4_1_3(
                tumorBams=self.bam,
                intervals=self.intervals,
                reference=self.reference,
                panelOfNormals=self.panel_of_normals,
                germlineResource=self.gnomad,
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
                bam=self.bam, sites=self.gnomad, intervals=self.intervals
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

        # normalise vcf
        self.step(
            "splitnormalisevcf",
            SplitMultiAlleleNormaliseVcf(
                compressedTabixVcf=self.filtermutect2calls.out, reference=self.reference
            ),
        )

        self.output("variants", source=self.mutect2.out)
        self.output("out_bam", source=self.mutect2.bam)
        self.output("out", source=self.splitnormalisevcf.out)
