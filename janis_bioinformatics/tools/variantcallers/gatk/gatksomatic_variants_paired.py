from datetime import date

from janis_core import String, WorkflowBuilder, Array
from janis_bioinformatics.tools import gatk4
from janis_bioinformatics.tools.common import SplitMultiAlleleNormaliseVcf
from janis_bioinformatics.tools.vcftools import VcfToolsvcftoolsLatest
from janis_bioinformatics.tools.htslib import TabixLatest
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow


class GatkSomaticVariantCallerPairedTargeted(BioinformaticsWorkflow):
    def id(self):
        return "GATK4_SomaticVariantCallerPairedTargeted"

    def friendly_name(self):
        return "GATK4 Somatic Variant Caller for Tumor/Normal Paired Samples with Targeted BED"

    def tool_provider(self):
        return "Variant Callers"

    def version(self):
        return "v0.1.0"

    def constructor(self):

        self.input("normal_bam", BamBai)
        self.input("tumor_bam", BamBai)

        self.input("normal_name", str)
        self.input("tumor_name", str)

        self.input(
            "targeted_bed",
            Bed(),
            doc="If this file resolves "
            "to null, then GATK will process the whole genome per each tool's spec",
        )

        self.input("reference", FastaWithDict)
        self.input("snps_dbsnp", VcfTabix)
        self.input("snps_1000gp", VcfTabix)
        self.input("known_indels", VcfTabix)
        self.input("mills_indels", VcfTabix)
        self.input("gnomad", VcfTabix)

        # # base calibration for normal and tumor bam
        self.step(
            "normal",
            self.process_subpipeline(
                bam=self.normal_bam,
                intervals=self.targeted_bed,
                reference=self.reference,
                known_sites=[
                    self.snps_dbsnp,
                    self.snps_1000gp,
                    self.known_indels,
                    self.mills_indels,
                ],
            ),
        )
        self.step(
            "tumor",
            self.process_subpipeline(
                bam=self.tumor_bam,
                intervals=self.targeted_bed,
                reference=self.reference,
                known_sites=[
                    self.snps_dbsnp,
                    self.snps_1000gp,
                    self.known_indels,
                    self.mills_indels,
                ],
            ),
        )

        # variant calling + learn read orientation model
        self.step(
            "mutect2",
            gatk4.GatkMutect2_4_1_3(
                normalBams=self.normal.out,
                tumorBams=self.tumor.out,
                normalSample=self.normal_name,
                intervals=self.targeted_bed,
                reference=self.reference,
                germlineResource=self.gnomad,
            ),
        )
        self.step(
            "learnorientationmoduel",
            gatk4.Gatk4LearnReadOrientationModelLatest(
                f1r2CountsFiles=self.mutect2.f1f2r_out,
            ),
        )

        # calculate contamination and segmentation
        self.step(
            "getpileupsummaries",
            gatk4.Gatk4GetPileUpSummariesLatest(
                bam=self.tumor_bam, sites=self.gnomad, intervals=self.targeted_bed
            ),
        )
        self.step(
            "calculatecontamination",
            gatk4.Gatk4CalculateContaminationLatest(
                pileupTable=self.getpileupsummaries.out,
                segmentationFileOut="tumor_segmentation.mutect2_segments",
            ),
        )
        self.step(
            "filtermutect2calls",
            gatk4.Gatk4FilterMutectCallsLatest(
                vcf=self.mutect2.out,
                reference=self.reference,
                segmentationFile=self.calculatecontamination.segOut,
                contaminationTable=self.calculatecontamination.contOut,
                readOrientationModel=self.learnorientationmoduel.out,
                statsFile=self.mutect2.stats,
            ),
        )

        # normalise and filter "PASS" variants
        self.step(
            "splitnormalisevcf",
            SplitMultiAlleleNormaliseVcf(
                compressedTabixVcf=self.filtermutect2calls.out, reference=self.reference
            ),
        )

        self.step(
            "fileterpass",
            VcfToolsvcftoolsLatest(
                compressedVcf=self.splitnormalisevcf.out,
                removeFileteredAll=True,
                recode=True,
                recodeINFOAll=True,
            ),
        )

        self.step("tabixvcf", TabixLatest(file=self.fileterpass.out))

        self.output("variants", source=self.mutect2.out)
        self.output("out", source=self.tabixvcf.out)

    @staticmethod
    def process_subpipeline(**connections):
        w = WorkflowBuilder("somatic_subpipeline")

        w.input("bam", BamBai)
        w.input("intervals", Bed)
        w.input("reference", FastaWithDict)
        w.input("known_sites", Array(VcfTabix))

        w.step(
            "base_recalibrator",
            gatk4.Gatk4BaseRecalibratorLatest(
                bam=w.bam,
                intervals=w.intervals,
                reference=w.reference,
                knownSites=w.known_sites,
            ),
        )

        w.step(
            "apply_bqsr",
            gatk4.Gatk4ApplyBqsrLatest(
                bam=w.bam,
                recalFile=w.base_recalibrator.out,
                intervals=w.intervals,
                reference=w.reference,
            ),
        )

        w.output("out", source=w.apply_bqsr.out)

        return w(**connections)
