from janis_bioinformatics.tools.illumina.manta.manta_1_4_0 import Manta_1_4_0
from . import TestBase


class TestManta(TestBase):

    def test_initial_manta(self):
        w = Manta_1_4_0()
        cwl = w.translate("cwl")
        task = self.run_task(source=cwl, inputs={
            "reference": {"class": "File",
                          "path": "/Users/franklinmichael/reference/hg38/assembly/Homo_sapiens_assembly38.fasta"},
            "bam": {"class": "File",
                    "path": "/Users/franklinmichael/Desktop/workflows-for-testing/strelka/inputs/BRCA1.bam"},
            "runDir": "out"
        })

        print(task.outputs)

        self.assertTrue(True)
