from datetime import date

from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.data_types import FastaWithDict, BamBai, BedTabix, VcfTabix

from janis_core import Array, Boolean, String

from janis_bioinformatics.tools.dawson import RefilterStrelka2Calls_0_1
from janis_bioinformatics.tools.dawson.workflows.strelka2passanalysisstep1 import (
    Strelka2PassWorkflowStep1,
)
from janis_bioinformatics.tools.dawson.workflows.strelka2passanalysisstep2 import (
    Strelka2PassWorkflowStep2,
)

from janis_bioinformatics.tools.htslib import BGZipLatest, TabixLatest


class Strelka2PassWorkflow(BioinformaticsWorkflow):
    def id(self):
        return "Strelka2PassWorkflow"

    def friendly_name(self):
        return "Strelka 2Pass analysis"

    @staticmethod
    def tool_provider():
        return "Dawson Labs"

    @staticmethod
    def version():
        return "0.1"

    def bind_metadata(self):
        self.metadata.version = "0.1"
        self.metadata.dateCreated = date(2019, 10, 11)
        self.metadata.dateUpdated = date(2019, 10, 15)

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

        self.input("normalBam", BamBai)
        self.input("tumorBams", Array(BamBai))

        self.input("reference", FastaWithDict)
        self.input("callRegions", BedTabix(optional=True))
        self.input("exome", Boolean(optional=True), default=False)

        self.input("sampleNames", Array(String, optional=True))

        self.step(
            "step1",
            Strelka2PassWorkflowStep1(
                normalBam=self.normalBam,
                tumorBam=self.tumorBams,
                reference=self.reference,
                callRegions=self.callRegions,
                exome=self.exome,
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
            ),
            scatter="tumorBam",
        )

        self.step(
            "refilterSNVs",
            RefilterStrelka2Calls_0_1(
                inputFiles=self.step2.snvs, sampleNames=self.sampleNames
            ),
        )
        self.step(
            "compressSNVs", BGZipLatest(file=self.refilterSNVs.out), scatter="file"
        )
        self.step("indexSNVs", TabixLatest(file=self.compressSNVs.out), scatter="file")

        self.step(
            "refilterINDELs",
            RefilterStrelka2Calls_0_1(
                inputFiles=self.step2.indels, sampleNames=self.sampleNames
            ),
        )
        self.step(
            "compressINDELs", BGZipLatest(file=self.refilterINDELs.out), scatter="file"
        )
        self.step(
            "indexINDELs", TabixLatest(file=self.compressINDELs.out), scatter="file"
        )

        self.output("snvs", source=self.indexSNVs)
        self.output("indels", source=self.indexINDELs)
        # once optional outputs are supported we should enable this again
        # self.output("svs", source=self.step1.somaticSVs)


if __name__ == "__main__":

    wf = Strelka2PassWorkflow()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
