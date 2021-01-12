from datetime import date

from janis_core import Array, String
from janis_bioinformatics.data_types import FastaWithDict, VcfTabix
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_core.operators.standard import FirstOperator

from janis_bioinformatics.tools.bcftools import (
    BcfToolsConcat_1_9 as BcfToolsConcat,
    BcfToolsIndex_1_9 as BcfToolsIndex,
    BcfToolsNorm_1_9 as BcfToolsNorm,
)
from janis_bioinformatics.tools.dawson.createcallregions.base import CreateCallRegions

from janis_bioinformatics.tools.gatk4 import (
    Gatk4CalculateContaminationLatest as CalculateContamination,
    Gatk4FilterMutectCallsLatest as FilterMutectCalls,
    Gatk4LearnReadOrientationModelLatest as LearnReadOrientationModel,
    Gatk4MergeMutectStatsLatest as MergeMutectStats,
)


class Mutect2JointSomaticWorkflow(BioinformaticsWorkflow):
    def id(self):
        return "Mutect2JointSomaticWorkflow"

    def friendly_name(self):
        return "Mutect2 joint somatic variant calling workflow"

    def tool_provider(self):
        return "Dawson Labs"

    def version(self):
        return "0.1.1"

    def bind_metadata(self):
        self.metadata.version = "0.1.1"
        self.metadata.dateCreated = date(2019, 10, 30)
        self.metadata.dateUpdated = date(2020, 12, 10)

        self.metadata.contributors = ["Sebastian Hollizeck"]
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

    # this is a way to get the tool without spagetti code in bam and cram format
    def getMutect2Tool(self):
        from janis_bioinformatics.tools.gatk4.mutect2.versions import (
            GatkMutect2_4_1_8 as Mutect2,
        )

        return Mutect2

    def getPileUpTool(self):
        from janis_bioinformatics.tools.gatk4.getpileupsummaries.versions import (
            Gatk4GetPileUpSummaries_4_1_8 as Pileup,
        )

        return Pileup

    def getMutect2InputType(self):
        from janis_bioinformatics.data_types import BamBai

        return BamBai

    def constructor(self):

        # we have to split the bam into the ones of the normal sample (can be multiple) and the
        # tumor, because some tools only work with the tumor bams
        self.input(
            "normalBams",
            Array(self.getMutect2InputType()),
            doc="The bams that make up the normal sample. Generally Mutect will expect one bam per sample, but as long as the sample ids in the bam header are set appropriatly, multiple bams per sample will work",
        )
        self.input(
            "tumorBams",
            Array(self.getMutect2InputType()),
            doc="The bams that contain the tumour samples. Generally Mutect will expect one bam per sample, but as long as the sample ids in the bam header are set appropriatly, multiple bams per sample will work",
        )

        # we also need the name of the normal sample (needs to be the name in the bams as well)
        self.input(
            "normalName",
            String,
            doc="The sample id of the normal sample. This id will be used to distingiush reads from this sample from all other samples. This id needs to tbe the one set in the bam header",
        )

        self.input(
            "biallelicSites",
            VcfTabix,
            doc="A vcf of common biallalic sites from a population. This will be used to estimate sample contamination.",
        )

        self.input(
            "reference",
            FastaWithDict,
            doc="A fasta and dict indexed reference, which needs to be the reference, the bams were aligned to.",
        )

        self.input(
            "regionSize",
            int,
            default=10000000,
            doc="The size of the regions over which to parallelise the analysis. This should be adjusted, if there are lots of samples or a very high sequencing depth. default: 10M bp",
        )

        self.input(
            "panelOfNormals",
            VcfTabix,
            doc="The panel of normals, which summarises the technical and biological sites of errors. Its usually a good idea to generate this for your own cohort, but GATK suggests around 30 normals, so their panel is usually a good idea.",
        )

        self.input(
            "germlineResource",
            VcfTabix,
            doc="Vcf of germline variants. GATK provides this as well, but it can easily substituted with the newst gnomad etc vcf.",
        )

        self.step(
            "createCallRegions",
            CreateCallRegions(
                reference=self.reference,
                regionSize=self.regionSize,
                equalize=True,
            ),
        )

        self.step(
            "mutect2",
            self.getMutect2Tool()(
                tumorBams=self.tumorBams,
                normalBams=self.normalBams,
                normalSample=self.normalName,
                intervals=self.createCallRegions.regions,
                reference=self.reference,
                panelOfNormals=self.panelOfNormals,
                germlineResource=self.germlineResource,
            ),
            scatter="intervals",
        )

        self.step("concat", BcfToolsConcat(vcf=self.mutect2.out))
        self.step("indexUnfiltered", BcfToolsIndex(vcf=self.concat.out))

        self.step(
            "learn", LearnReadOrientationModel(f1r2CountsFiles=self.mutect2.f1f2r_out)
        )

        self.step("mergeMutect2", MergeMutectStats(statsFiles=self.mutect2.stats))

        self.step(
            "pileup",
            self.getPileUpTool()(
                bam=self.tumorBams,
                sites=self.biallelicSites,
                intervals=self.biallelicSites,
                reference=self.reference,
            ),
        )

        self.step("contamination", CalculateContamination(pileupTable=self.pileup.out))

        self.step(
            "filtering",
            FilterMutectCalls(
                vcf=self.indexUnfiltered.out,
                reference=self.reference,
                segmentationFile=self.contamination.segOut,
                contaminationTable=self.contamination.contOut,
                readOrientationModel=self.learn.out,
                statsFile=self.mergeMutect2.out,
            ),
        )

        self.step(
            "normalise", BcfToolsNorm(vcf=self.filtering.out, reference=self.reference)
        )
        self.step("indexFiltered", BcfToolsIndex(vcf=self.normalise.out))
        self.output("out", source=self.indexFiltered.out)


if __name__ == "__main__":

    wf = Mutect2JointSomaticWorkflow()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
