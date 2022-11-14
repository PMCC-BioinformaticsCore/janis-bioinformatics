from datetime import date

from janis_bioinformatics.data_types import BedTabix, FastaFai
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.dawson import (
    RefilterStrelka2CallsLatest as RefilterStrelka2Calls,
)

from janis_bioinformatics.tools.htslib import BGZipLatest as BGZip, TabixLatest as Tabix
from janis_core import Array, Boolean, String, File, Int
from janis_bioinformatics.data_types import VcfTabix


class Strelka2PassWorkflow(BioinformaticsWorkflow):
    def id(self):
        return "Strelka2PassWorkflow"

    def friendly_name(self):
        return "Strelka 2Pass analysis"

    def tool_provider(self):
        return "Dawson Labs"

    def version(self):
        return "0.2"

    def bind_metadata(self):
        self.metadata.version = "0.2"
        self.metadata.dateCreated = date(2019, 10, 11)
        self.metadata.dateUpdated = date(2022, 5, 31)

        self.metadata.contributors = ["Sebastian Hollizeck"]
        self.metadata.keywords = [
            "variants",
            "strelka2",
            "variant caller",
            "multi sample",
        ]
        self.metadata.documentation = """
        This is the full 2pass analysis workflow to do joint somatic variant calling with strelka2.
        The idea is similar to the RNASeq 2pass analysis, when the input of the first analysis is used to guide the second analysis.

        The workflow will
         * run manta
         * run strelka with manata output
         * run strelka with strelka and manta output
         * reannotate the filter column
         * output resuults
                """.strip()

    # this is a way to get the tool without spagetti code in bam and cram format
    def getStep1Tool(self):
        from .steps.strelka2passanalysisstep1 import Strelka2PassWorkflowStep1

        return Strelka2PassWorkflowStep1

    def getStep2Tool(self):
        from .steps.strelka2passanalysisstep2 import Strelka2PassWorkflowStep2

        return Strelka2PassWorkflowStep2

    def getStrelka2InputType(self):
        from janis_bioinformatics.data_types import BamBai

        return BamBai

    def constructor(self):

        self.input(
            "normalBam",
            self.getStrelka2InputType(),
            doc="The bam of the normal sample. Strelka will assign any read in this bam to the normal sample, even if this bam contains multiple samples",
        )
        self.input(
            "tumorBams",
            Array(self.getStrelka2InputType()),
            doc="The bam of the tumour sample. Strelka will assign any read in this bam to the normal sample, even if this bam contains multiple samples",
        )

        self.input(
            "reference",
            FastaFai,
            doc="The fai indexed fasta reference, the bams were aligned to.",
        )

        self.input(
            "configStrelka",
            File(optional=True),
            doc="The possibly changed ini to use for Strelka2. This can be used to skip regions with extreme depth, like in heterochromatin regions, which lead to very long runtimes.",
        )
        self.input(
            "callRegions",
            BedTabix(optional=True),
            doc="The tabix indexed bed file of regions to restict the analysis on. If this is unset, every site in the genome will be analysed.",
        )
        self.input(
            "exome",
            Boolean(optional=True),
            default=False,
            doc="Sets the flag to analyse everything in exome mode. This will adjust the parameter for a non uniform coverage profile.",
        )

        self.input(
            "sampleNames",
            Array(String, optional=True),
            doc="The names of the tumour samples. This will only be used to rename output files. if unset, the output will be numbered in the same order as the input files.",
        )
        self.input(
            "minAD",
            Int(optional=True),
            default=2,
            doc="Minimum read support for a variant to be considered a true variant.",
        )

        self.step(
            "step1",
            self.getStep1Tool()(
                normalBam=self.normalBam,
                tumorBam=self.tumorBams,
                reference=self.reference,
                callRegions=self.callRegions,
                exome=self.exome,
                configStrelka=self.configStrelka,
            ),
            scatter="tumorBam",
        )

        self.step(
            "step2",
            self.getStep2Tool()(
                normalBam=self.normalBam,
                tumorBam=self.tumorBams,
                reference=self.reference,
                callRegions=self.callRegions,
                strelkaSNVs=self.step1.snvs,
                indelCandidates=self.step1.candIndels,
                # as soon as janis allows flattening of arguments, we need this
                # indelCandidates=self.step1.indels,
                exome=self.exome,
                configStrelka=self.configStrelka,
            ),
            scatter="tumorBam",
        )

        self.step(
            "refilterSNVs",
            RefilterStrelka2Calls(
                inputFiles=self.step2.snvs,
                minAD=self.minAD,
            ),
        )
        self.step("compressSNVs", BGZip(file=self.refilterSNVs.out), scatter="file")
        self.step("indexSNVs", Tabix(inp=self.compressSNVs.out), scatter="inp")

        self.step(
            "refilterINDELs",
            RefilterStrelka2Calls(
                inputFiles=self.step2.indels,
                minAD=self.minAD,
            ),
        )
        self.step("compressINDELs", BGZip(file=self.refilterINDELs.out), scatter="file")
        self.step("indexINDELs", Tabix(inp=self.compressINDELs.out), scatter="inp")

        self.output(
            "snvs",
            Array(VcfTabix),
            source=self.indexSNVs,
            output_folder=self.sampleNames,
        )
        self.output(
            "indels",
            Array(VcfTabix),
            source=self.indexINDELs,
            output_folder=self.sampleNames,
        )

        # optional output from manta, but we know it will be created
        self.output("svs", source=self.step1.somaticSVs, output_folder=self.sampleNames)


if __name__ == "__main__":

    wf = Strelka2PassWorkflow()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
