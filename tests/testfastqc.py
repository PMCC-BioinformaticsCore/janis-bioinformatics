from . import TestBase

from janis_bioinformatics.tools.babrahambioinformatics.fastqc.fastqc_0_11_5 import FastQC_0_11_5


class TestFastQC(TestBase):

    def test_fastqc(self):
        w = FastQC_0_11_5()
        cwl = w.translate("cwl")

        task = self.run_task(source=cwl, inputs={
            "read":
            # "/Users/franklinmichael/Desktop/workflows-for-testing/wgs/inputs/BRCA1_R1.fastq"
            {
                "class": "File",
                "path": "/Users/franklinmichael/Desktop/workflows-for-testing/wgs/inputs/BRCA1_R1.fastq"
            }
            # [
            #     {"class": "File",
            #      "path": "/Users/franklinmichael/Desktop/workflows-for-testing/wgs/inputs/BRCA1_R1.fastq"},
            #     {"class": "File",
            #      "path": "/Users/franklinmichael/Desktop/workflows-for-testing/wgs/inputs/BRCA1_R2.fastq"}
            # ]
        })

        print(task.outputs)

