from .combinevariants.versions import *
from .trimiupac.versions import *
from .parsefastqc.v0_1_0 import ParseFastqcAdaptors
from .performancesummary.versions import *
from .genecovpersample.versions import *
from .addsymtodepthofcoverage.versions import *
from .addbamstats.versions import *
from .extractstrelkasomaticaddp.versions import *
from .annotateDepthOfCoverageWorkflow import AnnotateDepthOfCoverage_0_1_0
from .performanceSummaryTargetedWorkflow import PerformanceSummaryTargeted_0_1_0
from .performanceSummaryGenomeWorkflow import PerformanceSummaryGenome_0_1_0
from .addBamStatsSomaticWorkflow import AddBamStatsSomatic_0_1_0
from .addBamStatsGermlineWorkflow import AddBamStatsGermline_0_1_0
from .molpathGermlineWorkflow import MolpathGermline_1_0_0
from .molpathTumorOnlyWorkflow import MolpathTumorOnly_1_0_0
from .generatevardictheaderlines import GenerateVardictHeaderLines
from .generatebedtoolscoveragegenomefile import GenerateGenomeFileForBedtoolsCoverage
from .generateintervalsbychromosome.generateintervalsbychromosome import (
    GenerateIntervalsByChromosome,
)
from .generatemantaconfig import GenerateMantaConfig
from .megafusion.versions import *
