from abc import ABC
from datetime import datetime
from janis_bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase

from janis_core import (
    CommandTool,
    ToolInput,
    ToolOutput,
    File,
    Boolean,
    String,
    Int,
    Double,
    Float,
    InputSelector,
    Filename,
    ToolMetadata,
    InputDocumentation,
)


class GatkModelSegmentsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "ModelSegments"

    def friendly_name(self) -> str:
        return "GATK4: ModelSegments"

    def tool(self) -> str:
        return "Gatk4ModelSegments"

    def inputs(self):
        return [
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Output directory. This will be created if it does not exist. Required."
                ),
            ),
            ToolInput(
                tag="outputPrefix",
                input_type=String(optional=True),
                prefix="--output-prefix",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Prefix for output filenames. Required."),
            ),
            ToolInput(
                tag="allelicCounts",
                input_type=File(optional=True),
                prefix="--allelic-counts",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input file containing allelic counts (output of CollectAllelicCounts). Default value: null. "
                ),
            ),
            ToolInput(
                tag="arguments_file",
                input_type=File(optional=True),
                prefix="--arguments_file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="read one or more arguments files and add them to the command line This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="denoisedCopyRatios",
                input_type=File(optional=True),
                prefix="--denoised-copy-ratios",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input file containing denoised copy ratios (output of DenoiseReadCounts). Default value: null. "
                ),
            ),
            ToolInput(
                tag="gatkConfigFile",
                input_type=String(optional=True),
                prefix="--gatk-config-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="A configuration file to use with the GATK. Default value: null."
                ),
            ),
            ToolInput(
                tag="gcsMaxRetries",
                input_type=Int(optional=True),
                prefix="--gcs-max-retries",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-gcs-retries)  If the GCS bucket channel errors out, how many times it will attempt to re-initiate the connection  Default value: 20. "
                ),
            ),
            ToolInput(
                tag="gcsProjectForRequesterPays",
                input_type=String(optional=True),
                prefix="--gcs-project-for-requester-pays",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Project to bill when accessing 'requester pays' buckets. If unset, these buckets cannot be accessed.  Default value: . "
                ),
            ),
            ToolInput(
                tag="genotypingBaseErrorRate",
                input_type=Double(optional=True),
                prefix="--genotyping-base-error-rate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum base-error rate for genotyping and filtering homozygous allelic counts, if available.  The likelihood for an allelic count to be generated from a homozygous site will be integrated from zero base-error rate up to this value.  Decreasing this value will increase the number of sites assumed to be heterozygous for modeling.  Default value: 0.05. "
                ),
            ),
            ToolInput(
                tag="genotypingHomozygousLogRatioThreshold",
                input_type=Double(optional=True),
                prefix="--genotyping-homozygous-log-ratio-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Log-ratio threshold for genotyping and filtering homozygous allelic counts, if available.  Increasing this value will increase the number of sites assumed to be heterozygous for modeling.  Default value: -10.0. "
                ),
            ),
            ToolInput(
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="kernelApproximationDimension",
                input_type=Int(optional=True),
                prefix="--kernel-approximation-dimension",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Dimension of the kernel approximation.  A subsample containing this number of data points will be used to construct the approximation for each chromosome.  If the total number of data points in a chromosome is greater than this number, then all data points in the chromosome will be used.  Time complexity scales quadratically and space complexity scales linearly with this parameter.  Default value: 100. "
                ),
            ),
            ToolInput(
                tag="kernelScalingAlleleFraction",
                input_type=Double(optional=True),
                prefix="--kernel-scaling-allele-fraction",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Relative scaling S of the kernel K_AF for allele-fraction segmentation to the kernel K_CR for copy-ratio segmentation.  If multidimensional segmentation is performed, the total kernel used will be K_CR + S * K_AF.  Default value: 1.0. "
                ),
            ),
            ToolInput(
                tag="kernelVarianceAlleleFraction",
                input_type=Double(optional=True),
                prefix="--kernel-variance-allele-fraction",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Variance of Gaussian kernel for allele-fraction segmentation, if performed.  If zero, a linear kernel will be used.  Default value: 0.025. "
                ),
            ),
            ToolInput(
                tag="kernelVarianceCopyRatio",
                input_type=Double(optional=True),
                prefix="--kernel-variance-copy-ratio",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Variance of Gaussian kernel for copy-ratio segmentation, if performed.  If zero, a linear kernel will be used.  Default value: 0.0. "
                ),
            ),
            ToolInput(
                tag="maximumNumberOfSegmentsPerChromosome",
                input_type=Int(optional=True),
                prefix="--maximum-number-of-segments-per-chromosome",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum number of segments allowed per chromosome.  Default value: 1000. "
                ),
            ),
            ToolInput(
                tag="maximumNumberOfSmoothingIterations",
                input_type=Int(optional=True),
                prefix="--maximum-number-of-smoothing-iterations",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum number of iterations allowed for segmentation smoothing.  Default value: 25. "
                ),
            ),
            ToolInput(
                tag="minimumTotalAlleleCountCase",
                input_type=Int(optional=True),
                prefix="--minimum-total-allele-count-case",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum total count for filtering allelic counts in the case sample, if available.  The default value of zero is appropriate for matched-normal mode; increase to an appropriate value for case-only mode.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="minimumTotalAlleleCountNormal",
                input_type=Int(optional=True),
                prefix="--minimum-total-allele-count-normal",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum total count for filtering allelic counts in the matched-normal sample, if available.  Default value: 30. "
                ),
            ),
            ToolInput(
                tag="minorAlleleFractionPriorAlpha",
                input_type=Double(optional=True),
                prefix="--minor-allele-fraction-prior-alpha",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Alpha hyperparameter for the 4-parameter beta-distribution prior on segment minor-allele fraction. The prior for the minor-allele fraction f in each segment is assumed to be Beta(alpha, 1, 0, 1/2). Increasing this hyperparameter will reduce the effect of reference bias at the expense of sensitivity.  Default value: 25.0. "
                ),
            ),
            ToolInput(
                tag="normalAllelicCounts",
                input_type=File(optional=True),
                prefix="--normal-allelic-counts",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input file containing allelic counts for a matched normal (output of CollectAllelicCounts).  Default value: null. "
                ),
            ),
            ToolInput(
                tag="numberOfBurnInSamplesAlleleFraction",
                input_type=Int(optional=True),
                prefix="--number-of-burn-in-samples-allele-fraction",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of burn-in samples to discard for allele-fraction model.  Default value: 50. "
                ),
            ),
            ToolInput(
                tag="numberOfBurnInSamplesCopyRatio",
                input_type=Int(optional=True),
                prefix="--number-of-burn-in-samples-copy-ratio",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of burn-in samples to discard for copy-ratio model.  Default value: 50. "
                ),
            ),
            ToolInput(
                tag="numberOfChangepointsPenaltyFactor",
                input_type=Double(optional=True),
                prefix="--number-of-changepoints-penalty-factor",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Factor A for the penalty on the number of changepoints per chromosome for segmentation.  Adds a penalty of the form A * C * [1 + log (N / C)], where C is the number of changepoints in the chromosome, to the cost function for each chromosome.  Must be non-negative.  Default value: 1.0. "
                ),
            ),
            ToolInput(
                tag="numberOfSamplesAlleleFraction",
                input_type=Int(optional=True),
                prefix="--number-of-samples-allele-fraction",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Total number of MCMC samples for allele-fraction model.  Default value: 100. "
                ),
            ),
            ToolInput(
                tag="numberOfSamplesCopyRatio",
                input_type=Int(optional=True),
                prefix="--number-of-samples-copy-ratio",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Total number of MCMC samples for copy-ratio model.  Default value: 100. "
                ),
            ),
            ToolInput(
                tag="numberOfSmoothingIterationsPerFit",
                input_type=Int(optional=True),
                prefix="--number-of-smoothing-iterations-per-fit",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of segmentation-smoothing iterations per MCMC model refit. (Increasing this will decrease runtime, but the final number of segments may be higher. Setting this to 0 will completely disable model refitting between iterations.)  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="smoothingCredibleIntervalThresholdAlleleFraction",
                input_type=Double(optional=True),
                prefix="--smoothing-credible-interval-threshold-allele-fraction",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of 10% equal-tailed credible-interval widths to use for allele-fraction segmentation smoothing.  Default value: 2.0. "
                ),
            ),
            ToolInput(
                tag="smoothingCredibleIntervalThresholdCopyRatio",
                input_type=Double(optional=True),
                prefix="--smoothing-credible-interval-threshold-copy-ratio",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of 10% equal-tailed credible-interval widths to use for copy-ratio segmentation smoothing.  Default value: 2.0. "
                ),
            ),
            ToolInput(
                tag="tmpDir",
                input_type=Boolean(optional=True),
                prefix="--tmp-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Temp directory to use. Default value: null."
                ),
            ),
            ToolInput(
                tag="useJdkDeflater",
                input_type=Boolean(optional=True),
                prefix="--use-jdk-deflater",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-jdk-deflater)  Whether to use the JdkDeflater (as opposed to IntelDeflater)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="useJdkInflater",
                input_type=Boolean(optional=True),
                prefix="--use-jdk-inflater",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-jdk-inflater)  Whether to use the JdkInflater (as opposed to IntelInflater)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--verbosity",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-verbosity)  Control verbosity of logging.  Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} "
                ),
            ),
            ToolInput(
                tag="version",
                input_type=Boolean(optional=True),
                prefix="--version",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="display the version number for this tool Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="windowSize",
                input_type=Int(optional=True),
                prefix="--window-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Window sizes to use for calculating local changepoint costs. For each window size, the cost for each data point to be a changepoint will be calculated assuming that the point demarcates two adjacent segments of that size.  Including small (large) window sizes will increase sensitivity to small (large) events.  Duplicate values will be ignored.  This argument may be specified 0 or more times. Default value: [8, 16, 32, 64, 128, 256]. "
                ),
            ),
            ToolInput(
                tag="showhidden",
                input_type=Boolean(optional=True),
                prefix="--showHidden",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-showHidden)  display hidden arguments  Default value: false. Possible values: {true, false} "
                ),
            ),
        ]

    def outputs(self):
        return []

    def metadata(self):
        return ToolMetadata(
            contributors=[],
            dateCreated=datetime.fromisoformat("2020-05-18T14:05:58.068520"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:05:58.068521"),
            documentation="USAGE: ModelSegments [arguments]\nModels segmented copy ratios from denoised read counts and segmented minor-allele fractions from allelic counts\nVersion:4.1.3.0\n",
        )
