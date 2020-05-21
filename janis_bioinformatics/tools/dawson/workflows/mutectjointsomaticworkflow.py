from datetime import date

from janis import Array, String
from janis_bioinformatics.data_types import CramCrai, FastaWithDict, VcfTabix
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import (
    BcfToolsConcat_1_9,
    BcfToolsIndex_1_9,
    BcfToolsNorm_1_9,
)
from janis_bioinformatics.tools.gatk4 import (
    Gatk4CalculateContamination_4_1_4,
    Gatk4FilterMutectCalls_4_1_4,
    Gatk4GetPileUpSummaries_4_1_4,
    Gatk4LearnReadOrientationModel_4_1_4,
    Gatk4MergeMutectStats_4_1_2,
)
from janis_bioinformatics.tools.gatk4.mutect2.versions_cram import GatkMutect2_4_1_4


class Mutect2JointSomaticWorkflow(BioinformaticsWorkflow):
    def id(self):
        return "Mutect2JointSomaticWorkflow"

    def friendly_name(self):
        return "Mutect2 joint somatic variant calling workflow"

    @staticmethod
    def tool_provider():
        return "Dawson Labs"

    @staticmethod
    def version():
        return "0.1"

    def bind_metadata(self):
        self.metadata.version = "0.1"
        self.metadata.dateCreated = date(2019, 10, 30)
        self.metadata.dateUpdated = date(2019, 10, 30)

        self.contributors = ["Sebastian Hollizeck"]
        self.metadata.keywords = [
            "variants",
            "mutect2",
            "variant caller",
            "multi sample",
        ]
        self.metadata.documentation = """
        This workflow uses the capability of mutect2 to call several samples at the same time and improve recall and accuracy through a joint model.
        Most of these tools are still in a beta state and not intended for main production (as of 4.1.4.0)
        There are also som major tweaks we have to do for runtime, as the amount of data might overwhelm the tools otherwise.
                """.strip()

    def constructor(self):

        # we have to split the bam into the ones of the normal sample (can be multiple) and the
        # tumor, because some tools only work with the tumor bams
        self.input("normalBams", Array(CramCrai))
        self.input("tumorBams", Array(CramCrai))

        # we also need the name of the normal sample (needs to be the name in the bams as well)
        self.input("normalName", String)

        self.input("biallelicSites", VcfTabix)

        self.input("reference", FastaWithDict)

        # exec(open("./regions.py").read())
        self.input("intervals", Array(String))

        self.input("panelOfNormals", VcfTabix)

        self.input("germlineResource", VcfTabix)

        self.step(
            "mutect2",
            GatkMutect2_4_1_4(
                tumorBams=self.tumorBams,
                normalBams=self.normalBams,
                normalSample=self.normalName,
                intervals=self.intervals,
                reference=self.reference,
                panelOfNormals=self.panelOfNormals,
                germlineResource=self.germlineResource,
            ),
            scatter="intervals",
        )

        self.step("concat", BcfToolsConcat_1_9(vcf=self.mutect2.out))
        self.step("indexUnfiltered", BcfToolsIndex_1_9(vcf=self.concat.out))

        self.step(
            "learn",
            Gatk4LearnReadOrientationModel_4_1_4(
                f1r2CountsFiles=self.mutect2.f1f2r_out
            ),
        )

        self.step(
            "mergeMutect2", Gatk4MergeMutectStats_4_1_2(statsFiles=self.mutect2.stats)
        )

        self.step(
            "pileup",
            Gatk4GetPileUpSummaries_4_1_4(
                bam=self.tumorBams, sites=self.biallelic, intervals=self.biallelic
            ),
        )

        self.step(
            "contamination",
            Gatk4CalculateContamination_4_1_4(pileupTable=self.pileup.out),
        )

        self.step(
            "filtering",
            Gatk4FilterMutectCalls_4_1_4(
                vcf=self.indexUnfiltered.out,
                reference=self.reference,
                segmentationFile=self.contamination.segOut,
                contaminationTable=self.contamination.contOut,
                readOrientationModel=self.learn.out,
                statsFile=self.mergeMutect2.out,
            ),
        )

        self.step(
            "normalise",
            BcfToolsNorm_1_9,
            vcf=self.filtering.out,
            reference=self.reference,
        )
        self.step("indexFiltered", BcfToolsIndex_1_9, vcf=self.normalise.out)
        self.output("out", source=self.indexFiltered.out)
