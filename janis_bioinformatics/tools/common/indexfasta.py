from janis_bioinformatics.data_types import Fasta
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bwa import BwaIndexLatest
from janis_bioinformatics.tools.gatk4 import Gatk4CreateSequenceDictionaryLatest
from janis_bioinformatics.tools.samtools.faidx.versions import SamToolsFaidxLatest


class IndexFasta(BioinformaticsWorkflow):
    def id(self):
        return "IndexFasta"

    def friendly_name(self):
        return "Index Fasta reference"

    def tool_provider(self):
        return "common"

    def version(self):
        return "1.0.0"

    def constructor(self):

        self.input("reference", Fasta)

        self.step("create_bwa", BwaIndexLatest(reference=self.reference))
        self.step("create_samtools", SamToolsFaidxLatest(reference=self.reference))
        self.step(
            "create_dict", Gatk4CreateSequenceDictionaryLatest(reference=self.reference)
        )

        self.output("bwa", source=self.create_bwa, output_name="reference")
        self.output("samtools", source=self.create_samtools, output_name="reference")
        self.output("dict", source=self.create_dict, output_name="reference")


if __name__ == "__main__":
    IndexFasta().translate("wdl")
