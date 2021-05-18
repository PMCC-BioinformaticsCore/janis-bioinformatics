import os
import operator
from janis_core import Array
from janis_bioinformatics.data_types import FastqGzPair, FastaWithDict
from janis_bioinformatics.tools import BioinformaticsWorkflow, BioinformaticsTool
from janis_bioinformatics.tools.common.bwamem_samtoolsview import BwaMem_SamToolsView
from janis_bioinformatics.tools.cutadapt import CutAdapt_2_1
from janis_bioinformatics.tools.gatk4 import Gatk4SortSam_4_1_2
from janis_bioinformatics.data_types.bam import Bam, BamBai

from janis_core.tool.test_classes import (
    TTestPreprocessor,
    TTestExpectedOutput,
    TTestCase,
)


class BwaAligner(BioinformaticsWorkflow):
    def id(self):
        return "BwaAligner"

    def friendly_name(self):
        return "Align and sort reads"

    def tool_provider(self):
        return "common"

    def version(self):
        return "1.0.0"

    def constructor(self):
        # Inputs
        self.input("sample_name", str)
        self.input("reference", FastaWithDict)
        self.input("fastq", FastqGzPair)

        # pipe adapters
        self.input("cutadapt_adapter", Array(str, optional=True))
        self.input("cutadapt_removeMiddle3Adapter", Array(str, optional=True))

        # Steps
        self.step(
            "cutadapt",
            CutAdapt_2_1(
                fastq=self.fastq,
                adapter=self.cutadapt_adapter,
                front=None,
                removeMiddle5Adapter=None,
                removeMiddle3Adapter=self.cutadapt_removeMiddle3Adapter,
                qualityCutoff=15,
                minimumLength=50,
                outputPrefix=self.sample_name,
            ),
        )

        self.step(
            "bwamem",
            BwaMem_SamToolsView(
                reads=self.cutadapt.out,
                sampleName=self.sample_name,
                reference=self.reference,
                markShorterSplits=True,
            ),
        )

        self.step(
            "sortsam",
            Gatk4SortSam_4_1_2(
                bam=self.bwamem.out,
                sortOrder="coordinate",
                createIndex=True,
                validationStringency="SILENT",
                maxRecordsInRam=5000000,
                tmpDir=".",
            ),
        )

        # outputs
        self.output("out", source=self.sortsam)

    def bind_metadata(self):
        self.metadata.documentation = "Align sorted bam with this subworkflow consisting of BWA Mem + SamTools + Gatk4SortSam"
        self.metadata.contributors = ["Michael Franklin"]
        self.metadata.dateCreated = "2018-12-24"
        self.metadata.version = "1.1"

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "sample_name": "NA12878-BRCA1",
                    "fastq": [
                        os.path.join(
                            BioinformaticsTool.test_data_path(),
                            "wgsgermline_data",
                            "NA12878-BRCA1_R1.fastq.gz",
                        ),
                        os.path.join(
                            BioinformaticsTool.test_data_path(),
                            "wgsgermline_data",
                            "NA12878-BRCA1_R2.fastq.gz",
                        ),
                    ],
                    "reference": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.chr17.fasta",
                    ),
                    "cutadapt_qualityCutoff": 15,
                    "cutadapt_minimumLength": 50,
                    "bwamem_markShorterSplits": True,
                    "sortsam_sortOrder": "coordinate",
                    "sortsam_createIndex": True,
                    "sortsam_maxRecordsInRam": 5000000,
                    "sortsam_tmpDir": "./tmp",
                    "sortsam_validationStringency": "SILENT",
                },
                output=BamBai.basic_test(
                    "out",
                    2826000,
                    49688,
                    os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.bam.flagstat",
                    ),
                ),
            ),
            TTestCase(
                name="minimal",
                input={
                    "sample_name": "NA12878-BRCA1",
                    "fastq": [
                        os.path.join(
                            BioinformaticsTool.test_data_path(),
                            "wgsgermline_data",
                            "NA12878-BRCA1_R1.fastq.gz",
                        ),
                        os.path.join(
                            BioinformaticsTool.test_data_path(),
                            "wgsgermline_data",
                            "NA12878-BRCA1_R2.fastq.gz",
                        ),
                    ],
                    "reference": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "Homo_sapiens_assembly38.chr17.fasta",
                    ),
                    "cutadapt_qualityCutoff": 15,
                    "cutadapt_minimumLength": 50,
                    "bwamem_markShorterSplits": True,
                    "sortsam_sortOrder": "coordinate",
                    "sortsam_createIndex": True,
                    "sortsam_maxRecordsInRam": 5000000,
                    "sortsam_tmpDir": "./tmp",
                    "sortsam_validationStringency": "SILENT",
                },
                output=self.minimal_test(),
            ),
        ]


if __name__ == "__main__":
    w = BwaAligner()

    w.translate("wdl", with_resource_overrides=True)

    # print(build_resources_input(w, "wdl", {CaptureType.KEY: CaptureType.CHROMOSOME}))

    # print(AlignSortedBam().help())

    # import shepherd
    #
    # task = shepherd.from_workflow(w, engine=shepherd.Cromwell(), env="pmac")
    # print(task.outputs)
