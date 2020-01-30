from datetime import date

from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.data_types import (
    FastaWithDict,
    BamBai,
    BedTabix,
    VcfTabix,
    CramCrai,
)

from janis_core import Array, Boolean, String, Int, Filename

from janis_bioinformatics.tools.dawson import CallSomaticFreeBayes_0_1
from janis_bioinformatics.tools.freebayes import FreeBayes_1_3

from janis_bioinformatics.tools.htslib import BGZipLatest, TabixLatest
from janis_bioinformatics.tools.bcftools import BcfToolsNormLatest, BcfToolsSortLatest

from janis_bioinformatics.tools.vcflib import (
    VcfUniqLatest,
    VcfFixUpLatest,
    VcfUniqAllelesLatest,
    VcfAllelicPrimitivesLatest,
    VcfCombineLatest,
    VcfStreamSortLatest,
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
        self.metadata.dateUpdated = date(2019, 10, 25)

        self.contributors = ["Sebastian Hollizeck"]
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

        self.input("bams", Array(CramCrai))

        self.input("reference", FastaWithDict)
        self.input(
            "callRegions",
            Array(String, optional=True),
            default=[
                "chr1",
                "chr2",
                "chr3",
                "chr4",
                "chr5",
                "chr6",
                "chr7",
                "chr8",
                "chr9",
                "chr10",
                "chr11",
                "chr12",
                "chr13",
                "chr14",
                "chr15",
                "chr16",
                "chr17",
                "chr18",
                "chr19",
                "chr20",
                "chr21",
                "chr22",
                "chrX",
                "chrY",
                "chrM",
            ],
        )

        self.input("normalSample", String)
        self.input("sampleNames", Array(String, optional=True))

        self.input("skipCov", Int(optional=True), default=500)

        self.step(
            "callVariants",
            FreeBayes_1_3(
                bams=self.bams,
                reference=self.reference,
                pooledDiscreteFlag=True,
                gtQuals=True,
                strictFlag=True,
                pooledContinousFlag=True,
                reportMaxGLFlag=True,
                noABPriorsFlag=True,
                maxNumOfAlleles=5,
                noPartObsFlag=True,
                region=self.callRegions,
                skipCov=self.skipCov,
                # things that are actually default, but janis does not recognize yet
                useDupFlag=False,
                minBaseQual=0,
                minSupQsum=0,
                minSupMQsum=0,
                minAltQSum=0,
                minCov=0,
            ),
            scatter="region",
        )
        # might actually rewrite this once everything works, to not combine the files here, but do
        # all of it scattered and then only combine the final output
        # self.step("combineRegions", VcfCombineLatest(vcf=self.callVariants.out))

        #

        # self.step("compressAll", BGZipLatest(file=self.sortAll.out))
        # self.step("indexAll", TabixLatest(file=self.compressAll.out))

        self.step(
            "callSomatic",
            CallSomaticFreeBayes_0_1(
                vcf=self.callVariants.out, normalSampleName=self.normalSample
            ),
            # added for parallel
            scatter="vcf",
        )

        self.step("combineRegions", VcfCombineLatest(vcf=self.callSomatic.out))

        # should not be necessary here, but just to be save
        self.step(
            "sortSomatic1",
            VcfStreamSortLatest(vcf=self.combineRegions.out, inMemoryFlag=True),
        )

        # no need to compress this here if it leads to problems when we dont have an index for the allelic allelicPrimitves
        self.step(
            "normalizeSomatic1",
            BcfToolsNormLatest(
                vcf=self.sortSomatic1.out,
                reference=self.reference,
                outputType="v",
                outputFilename="normalised.vcf",
            ),
        )

        self.step(
            "allelicPrimitves",
            VcfAllelicPrimitivesLatest(
                vcf=self.normalizeSomatic1.out,
                tagParsed="DECOMPOSED",
                keepGenoFlag=True,
            ),
        )

        self.step("fixSplitLines", VcfFixUpLatest(vcf=self.allelicPrimitves.out))

        self.step(
            "sortSomatic2",
            VcfStreamSortLatest(vcf=self.fixSplitLines.out, inMemoryFlag=True),
        )

        self.step(
            "normalizeSomatic2",
            BcfToolsNormLatest(
                vcf=self.sortSomatic2.out,
                reference=self.reference,
                outputType="v",
                outputFilename="normalised.vcf",
            ),
        )

        self.step("uniqueAlleles", VcfUniqAllelesLatest(vcf=self.normalizeSomatic2.out))

        self.step(
            "sortFinal",
            VcfStreamSortLatest(vcf=self.uniqueAlleles.out, inMemoryFlag=True),
        )

        self.step("uniqVcf", VcfUniqLatest(vcf=self.sortFinal.out))

        self.step("compressFinal", BGZipLatest(file=self.uniqVcf.out))

        self.step("indexFinal", TabixLatest(file=self.compressFinal.out))

        self.output("outVcf", source=self.indexFinal)


if __name__ == "__main__":

    wf = FreeBayesSomaticWorkflow()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
