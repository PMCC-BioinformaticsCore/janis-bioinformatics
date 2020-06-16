from janis_bioinformatics.utils.typeconversion import cast_input_bams_to_crams
from janis_core import String

from .base_4_1 import Gatk4Mutect2Base_4_1


class Gatk4Mutect2CramBase_4_1(Gatk4Mutect2Base_4_1):
    def inputs(self):
        # we want every input which is a bam in the original to be a cram now
        ins = cast_input_bams_to_crams(super().inputs())

        # for this workflow to work, the intervals needs to be a string and not a file so we change
        # this here as well (GATK allows both a bed file or a samtools like region string)
        for inp in ins:
            if inp.id() == "intervals":
                # getting original optional status
                is_optional = inp.input_type.optional
                # set to string
                inp.input_type = String()
                # restore original optionality
                inp.input_type.optional = is_optional

        return ins
