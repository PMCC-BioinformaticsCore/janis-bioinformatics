
from janis_bioinformatics.tools.htslib import Tabix_1_2_1
from . import TestBase


class TestTabix(TestBase):

    def test_tabix(self):
        w = Tabix_1_2_1()
        cwl = w.translate("cwl")
        task = self.run_task(source=cwl, inputs={
            "file":
                "/Users/franklinmichael/Desktop/workflows-for-testing/tabix/inputs/inp.vcf.gz"
            # {
            #     "class": "File",
            #     "path": "/Users/franklinmichael/Desktop/workflows-for-testing/tabix/inputs/inp.vcf.gz"
            # }
        })

        print(task.outputs)

if __name__ == "__main__":
    print(Tabix_1_2_1().translate("cwl"))
