from janis import Step, Input, Output

from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.htslib import BGZip_1_2_1, Tabix_1_2_1


class CompressVCF(BioinformaticsWorkflow):
    def __init__(self):
        super(CompressVCF, self).__init__("compressVCF", friendly_name="Compress VCF File")

        inp = Input("vcf", Vcf(), "/Users/franklinmichael/reference/hg38/snps_dbsnp/Homo_sapiens_assembly38.dbsnp138.compressable.vcf")

        s1_bgzip = Step("s1_bgzip", BGZip_1_2_1())
        s2_tabix = Step("s2_tabix", Tabix_1_2_1())

        self.add_edges([
            (inp, s1_bgzip.file),
            (s1_bgzip.out, s2_tabix.file)
        ])

        self.add_edges([
            (s2_tabix.out, Output("ret"))
        ])


if __name__ == "__main__":
    print(CompressVCF().dump_translation("cwl", to_disk=True, write_inputs_file=True))