from janis_bioinformatics.utils.typeconversion import cast_input_bams_to_crams

from .base import Gatk4GetPileUpSummariesBase


class Gatk4GetPileUpSummariesCramBase(Gatk4GetPileUpSummariesBase):
    def inputs(self):
        # we want every input which is a bam in the original to be a cram now
        return cast_input_bams_to_crams(super().inputs())
