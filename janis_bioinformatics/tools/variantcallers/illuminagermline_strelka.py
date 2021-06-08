from datetime import datetime
from janis_core import Boolean, WorkflowMetadata, File
from janis_unix.tools import UncompressArchive

from janis_bioinformatics.data_types import (
    FastaWithDict,
    BamBai,
    BedTabix,
    CompressedVcf,
)
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAllele
from janis_bioinformatics.tools.illumina import StrelkaGermline_2_9_10, Manta_1_5_0
from janis_bioinformatics.tools.vcftools import VcfToolsvcftoolsLatest


class IlluminaGermlineVariantCaller(BioinformaticsWorkflow):
    def id(self):
        return "strelkaGermlineVariantCaller"

    def friendly_name(self):
        return "Strelka Germline Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def version(self):
        return "v0.1.1"

    def constructor(self):

        self.input("bam", BamBai)
        self.input("reference", FastaWithDict)

        # optional
        self.input("intervals", BedTabix(optional=True))
        self.input("is_exome", Boolean(optional=True))
        self.input("manta_config", File(optional=True))
        self.input("strelka_config", File(optional=True))

        self.step(
            "manta",
            Manta_1_5_0(
                bam=self.bam,
                reference=self.reference,
                callRegions=self.intervals,
                exome=self.is_exome,
                config=self.manta_config,
            ),
        )

        self.step(
            "strelka",
            StrelkaGermline_2_9_10(
                bam=self.bam,
                reference=self.reference,
                callRegions=self.intervals,
                exome=self.is_exome,
                config=self.strelka_config,
            ),
        )

        # normalise and filter "PASS" variants
        self.step(
            "splitnormalisevcf",
            SplitMultiAllele(
                vcf=self.strelka.variants.as_type(CompressedVcf),
                reference=self.reference,
            ),
        )

        self.step(
            "filterpass",
            VcfToolsvcftoolsLatest(
                vcf=self.splitnormalisevcf.out,
                removeFileteredAll=True,
                recode=True,
                recodeINFOAll=True,
            ),
        )

        self.output("sv", source=self.manta.diploidSV)
        self.output("variants", source=self.strelka.variants)
        self.output("out", source=self.filterpass.out)

    def bind_metadata(self):
        return WorkflowMetadata(
            contributors=["Jiaan Yu", "Michael Franklin"],
            dateCreated=datetime(2019, 3, 28),
            dateUpdated=datetime(2021, 5, 27),
            documentation="",
        )


if __name__ == "__main__":

    wf = IlluminaGermlineVariantCaller()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
