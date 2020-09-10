from datetime import date

from janis_bioinformatics.data_types import BedTabix, CramCrai, FastaFai
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.dawson import (
    RefilterStrelka2Calls_0_1 as RefilterStrelka2Calls,
)
from janis_bioinformatics.tools.dawson.workflows.strelka2passanalysisstep1 import (
    Strelka2PassWorkflowStep1,
)
from janis_bioinformatics.tools.dawson.workflows.strelka2passanalysisstep2 import (
    Strelka2PassWorkflowStep2,
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
        return "0.1"

    def bind_metadata(self):
        self.metadata.version = "0.1"
        self.metadata.dateCreated = date(2019, 10, 11)
        self.metadata.dateUpdated = date(2020, 8, 4)

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

    def constructor(self):

        self.input("normalBam", CramCrai)
        self.input("tumorBams", Array(CramCrai))

        self.input("reference", FastaFai)

        self.input("configStrelka", File(optional=True))
        self.input("callRegions", BedTabix(optional=True))
        self.input("exome", Boolean(optional=True), default=False)

        self.input("sampleNames", Array(String, optional=True))
        self.input("minAD", Int(optional=True), default=2)

        self.step(
            "step1",
            Strelka2PassWorkflowStep1(
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
            Strelka2PassWorkflowStep2(
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
                sampleNames=self.sampleNames,
                minAD=self.minAD,
            ),
        )
        self.step("compressSNVs", BGZip(file=self.refilterSNVs.out), scatter="file")
        self.step("indexSNVs", Tabix(inp=self.compressSNVs.out), scatter="inp")

        self.step(
            "refilterINDELs",
            RefilterStrelka2Calls(
                inputFiles=self.step2.indels, sampleNames=self.sampleNames
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
