from janis_bioinformatics.data_types import Bam, BamBai, Cram, CramCrai
from janis_core import Array, String

from .base_4_1 import Gatk4Mutect2Base_4_1


class Gatk4Mutect2CramBase_4_1(Gatk4Mutect2Base_4_1):
    def inputs(self):
        # we want every input which is a bam in the original to be a cram now (with index if the bam had an index)
        ins = super().inputs()
        for inp in ins:
            # we need to check for BamBai first, as due to inheritance, the bambai is also a bam
            if isinstance(inp.input_type, BamBai):
                inp.input_type = CramCrai()
            elif isinstance(inp.input_type, Bam):
                inp.input_type = Cram()
            elif isinstance(inp.input_type, Array) and isinstance(
                inp.input_type.subtype(), BamBai
            ):
                inp.input_type = Array(CramCrai)
            elif isinstance(inp.input_type, Array) and isinstance(
                inp.input_type.subtype(), Bam
            ):
                inp.input_type = Array(Cram)
            elif inp.id() == "intervals":
                inp.input_type = String()
        return ins
