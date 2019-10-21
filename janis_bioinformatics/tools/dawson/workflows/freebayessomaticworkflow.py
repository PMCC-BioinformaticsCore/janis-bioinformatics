from datetime import date

from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.data_types import FastaWithDict, BamBai, BedTabix, VcfTabix

from janis_core import Array, Boolean, String

from janis_bioinformatics.tools.dawson import CallSomaticFreeBayes_0_1
from janis_bioinformatics.tools.freebayes import FreeBayes_1_2

from janis_bioinformatics.tools.htslib import BGZipLatest, TabixLatest
from janis_bioinformatics.tools.bcftools import (
    BcfToolsConcatLatest,
    BcfToolsNormLatest,
    BcfToolsSortLatest,
)

from janis_bioinformatics.tools.vcflib import (
    VcfSplitAllelicPrimitivesLatest,
    VcfFixUpLatest,
    VcfUniqAllelesLatest,
    VcfUniqLatest,
)


class FreeBayesSomaticWorkflow(BioinformaticsWorkflow):
    def id(self):
        return "FreeBayesSomaticWorkflow"

    def friendly_name(self):
        return "Freebayes somatic workflow"

    @staticmethod
    def tool_provider():
        return "Dawson Labs"

    @staticmethod
    def version():
        return "0.1"

    def bind_metadata(self):
        self.metadata.version = "0.1"
        self.metadata.dateCreated = date(2019, 10, 18)
        self.metadata.dateUpdated = date(2019, 10, 18)

        self.metadata.maintainer = "Sebastian Hollizeck"
        self.metadata.maintainerEmail = "sebastian.hollizeck@petermac.org"
        self.metadata.keywords = [
            "variants",
            "freebayes",
            "variant caller",
            "multi sample",
        ]
        self.metadata.documentation = """
        This workflow uses the capabilities of freebayes to output all variants independent of the
        diploid model which then in turn allows us to create a likelihood based difference between
        the normal sample and an arbitrary amount of samples.
        This allows a joint somatic genotyping of multiple samples of the same individual.
                """.strip()

    def constructor(self):

        self.input("bams", Array(BamBai))

        self.input("reference", FastaWithDict)
        self.input("callRegions", Array(String, optional=True))

        self.input("normalSample", String)
        self.input("sampleNames", Array(String, optional=True))

        self.step(
            "callVariants",
            FreeBayes_1_2(
                bams=self.bams,
                reference=self.reference,
                pooledDiscreteFlag=True,
                gtQuals=True,
                strictFlag=True,
                pooledContinousFlag=True,
                repoprtMaxGLFlag=True,
                noABPriorsFlag=True,
                maxNumOfAlleles=5,
                noPartObsFlag=True,
                region=self.callRegions,
            ),
            scatter="region",
        )

        self.step(
            "combine",
            BcfToolsConcatLatest(file=self.callVariants.out, allowOverLaps=True),
        )

        self.step("sort_all", BcfToolsSortLatest(file=self.combine.out))

        self.step("compress", BGZipLatest(file=self.sort_all.out))

        self.step("index_all", TabixLatest(file=self.compress_all.out))

        self.step(
            "callSomatic",
            CallSomaticFreeBayes_0_1(
                vcf=self.index_all.out,
                normalSampleName=self.normalSample,
                outFileName=self.normalSample + "somatic_calls.vcf",
            ),
        )

        self.step("normalization_first", BcfToolsNormLatest(file=self.callSomatic.out))

        self.step(
            "split_allelic_primitves",
            VcfSplitAllelicPrimitivesLatest(
                vcf=self.normalization_first, tagParsed="DECOMPOSED"
            ),
        )

        self.step(
            "fix_split_lines", VcfFixUpLatest(vcf=self.split_allelic_primitves.out)
        )

        self.step("sort_somatic", BcfToolsSortLatest(file=self.fix_split_lines.out))

        self.step(
            "normalization_second", BcfToolsNormLatest(file=self.sort_somatic.out)
        )

        self.step(
            "unique_alleles", VcfUniqAllelesLatest(vcf=self.normalization_second.out)
        )

        self.step("sort_final", BcfToolsSortLatest(file=self.unique_alleles.out))

        self.step("unique", VcfUniqLatest(vcf=self.sort_final.out))

        self.step("compress_final", BGZipLatest(file=self.unique.out))

        self.step("index_final", TabixLatest(file=self.compress_final.out))

        self.output("out", source=self.index_final)


if __name__ == "__main__":

    wf = FreeBayesSomaticWorkflow()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
