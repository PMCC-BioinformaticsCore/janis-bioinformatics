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


class GatkGermlineCNVCallerBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "GermlineCNVCaller"

    def friendly_name(self) -> str:
        return "GATK4: GermlineCNVCaller"

    def tool(self) -> str:
        return "Gatk4GermlineCNVCaller"

    def inputs(self):
        return [
            ToolInput(
                tag="contigPloidyCalls",
                input_type=File(optional=True),
                prefix="--contig-ploidy-calls",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input contig-ploidy calls directory (output of DetermineGermlineContigPloidy). Required."
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--input",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input read-count files containing integer read counts in genomic intervals for all samples.  All intervals specified via -L must be contained; if none are specified, then intervals must be identical and in the same order for all samples.  This argument must be specified at least once. Required. "
                ),
            ),
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
                tag="runMode",
                input_type=Boolean(optional=True),
                prefix="--run-mode",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Tool run-mode. Required. Possible values: {COHORT, CASE}"
                ),
            ),
            ToolInput(
                tag="activeClassPaddingHybridMode",
                input_type=Int(optional=True),
                prefix="--active-class-padding-hybrid-mode",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If copy-number-posterior-expectation-mode is set to HYBRID, CNV-active intervals determined at any time will be padded by this value (in the units of bp) in order to obtain the set of intervals on which copy number posterior expectation is performed exactly.  Default value: 50000. "
                ),
            ),
            ToolInput(
                tag="adamaxBeta1",
                input_type=Double(optional=True),
                prefix="--adamax-beta-1",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Adamax optimizer first moment estimation forgetting factor. Default value: 0.9."
                ),
            ),
            ToolInput(
                tag="adamaxBeta2",
                input_type=Double(optional=True),
                prefix="--adamax-beta-2",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Adamax optimizer second moment estimation forgetting factor. Default value: 0.99."
                ),
            ),
            ToolInput(
                tag="annotatedIntervals",
                input_type=File(optional=True),
                prefix="--annotated-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input annotated-intervals file containing annotations for GC content in genomic intervals (output of AnnotateIntervals).  All intervals specified via -L must be contained.  This input should not be provided if an input denoising-model directory is given (the latter already contains the annotated-interval file).  Default value: null. "
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
                tag="callerExternalAdmixingRate",
                input_type=Double(optional=True),
                prefix="--caller-external-admixing-rate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Admixing ratio of new and old called posteriors (between 0 and 1; larger values implies using more of the new posterior and less of the old posterior) after convergence.  Default value: 1.0. "
                ),
            ),
            ToolInput(
                tag="callerInternalAdmixingRate",
                input_type=Double(optional=True),
                prefix="--caller-internal-admixing-rate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Admixing ratio of new and old called posteriors (between 0 and 1; larger values implies using more of the new posterior and less of the old posterior) for internal convergence loops.  Default value: 0.75. "
                ),
            ),
            ToolInput(
                tag="callerUpdateConvergenceThreshold",
                input_type=Double(optional=True),
                prefix="--caller-update-convergence-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum tolerated calling update size for convergence.  Default value: 0.001. "
                ),
            ),
            ToolInput(
                tag="classCoherenceLength",
                input_type=Double(optional=True),
                prefix="--class-coherence-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Coherence length of CNV-active and CNV-silent domains (in the units of bp).  Default value: 10000.0. "
                ),
            ),
            ToolInput(
                tag="cnvCoherenceLength",
                input_type=Boolean(optional=True),
                prefix="--cnv-coherence-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 10000.0."),
            ),
            ToolInput(
                tag="convergenceSnrAveragingWindow",
                input_type=Int(optional=True),
                prefix="--convergence-snr-averaging-window",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Averaging window for calculating training signal-to-noise ratio (SNR) for convergence checking.  Default value: 500. "
                ),
            ),
            ToolInput(
                tag="convergenceSnrCountdownWindow",
                input_type=Int(optional=True),
                prefix="--convergence-snr-countdown-window",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The number of ADVI iterations during which the SNR is required to stay below the set threshold for convergence.  Default value: 10. "
                ),
            ),
            ToolInput(
                tag="convergenceSnrTriggerThreshold",
                input_type=Double(optional=True),
                prefix="--convergence-snr-trigger-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The SNR threshold to be reached before triggering the convergence countdown.  Default value: 0.1. "
                ),
            ),
            ToolInput(
                tag="copyNumberPosteriorExpectationMode",
                input_type=String(optional=True),
                prefix="--copy-number-posterior-expectation-mode",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The strategy for calculating copy number posterior expectations in the coverage denoising model.  Default value: HYBRID. Possible values: {MAP, EXACT, HYBRID} "
                ),
            ),
            ToolInput(
                tag="depthCorrectionTau",
                input_type=Boolean(optional=True),
                prefix="--depth-correction-tau",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 10000.0."),
            ),
            ToolInput(
                tag="disableAnnealing",
                input_type=Boolean(optional=True),
                prefix="--disable-annealing",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(advanced) Disable annealing. Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="disableCaller",
                input_type=Boolean(optional=True),
                prefix="--disable-caller",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(advanced) Disable caller. Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="disableSampler",
                input_type=Boolean(optional=True),
                prefix="--disable-sampler",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(advanced) Disable sampler. Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="enableBiasFactors",
                input_type=Boolean(optional=True),
                prefix="--enable-bias-factors",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Default value: true. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="excludeIntervals",
                input_type=Boolean(optional=True),
                prefix="--exclude-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-XL) This argument may be specified 0 or more times. Default value: null. "
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
                tag="gcCurveStandardDeviation",
                input_type=Double(optional=True),
                prefix="--gc-curve-standard-deviation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Prior standard deviation of the GC curve from flat.  Default value: 1.0. "
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
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="initArdRelUnexplainedVariance",
                input_type=Double(optional=True),
                prefix="--init-ard-rel-unexplained-variance",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Initial value of ARD prior precisions relative to the scale of interval-specific unexplained variance.  Default value: 0.1. "
                ),
            ),
            ToolInput(
                tag="initialTemperature",
                input_type=Double(optional=True),
                prefix="--initial-temperature",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Initial temperature (for DA-ADVI). Default value: 1.5."
                ),
            ),
            ToolInput(
                tag="intervalExclusionPadding",
                input_type=Int(optional=True),
                prefix="--interval-exclusion-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ixp)  Amount of padding (in bp) to add to each interval you are excluding.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="intervalMergingRule",
                input_type=Boolean(optional=True),
                prefix="--interval-merging-rule",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-imr)  Interval merging rule for abutting intervals  Default value: ALL. Possible values: {ALL, OVERLAPPING_ONLY} "
                ),
            ),
            ToolInput(
                tag="intervalPadding",
                input_type=Boolean(optional=True),
                prefix="--interval-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-ip) Default value: 0."),
            ),
            ToolInput(
                tag="intervalPsiScale",
                input_type=Double(optional=True),
                prefix="--interval-psi-scale",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Typical scale of interval-specific unexplained variance. Default value: 0.001."
                ),
            ),
            ToolInput(
                tag="intervalSetRule",
                input_type=Boolean(optional=True),
                prefix="--interval-set-rule",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-isr)  Set merging approach to use for combining interval inputs  Default value: UNION. Possible values: {UNION, INTERSECTION} "
                ),
            ),
            ToolInput(
                tag="intervals",
                input_type=String(optional=True),
                prefix="--intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-L) One or more genomic intervals over which to operate This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="learningRate",
                input_type=Double(optional=True),
                prefix="--learning-rate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Adamax optimizer learning rate. Default value: 0.01."
                ),
            ),
            ToolInput(
                tag="logEmissionSamplesPerRound",
                input_type=Int(optional=True),
                prefix="--log-emission-samples-per-round",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Log emission samples drawn per round of sampling.  Default value: 50. "
                ),
            ),
            ToolInput(
                tag="logEmissionSamplingMedianRelError",
                input_type=Double(optional=True),
                prefix="--log-emission-sampling-median-rel-error",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum tolerated median relative error in log emission sampling.  Default value: 0.005. "
                ),
            ),
            ToolInput(
                tag="logEmissionSamplingRounds",
                input_type=Int(optional=True),
                prefix="--log-emission-sampling-rounds",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Log emission maximum sampling rounds.  Default value: 10. "
                ),
            ),
            ToolInput(
                tag="logMeanBiasStandardDeviation",
                input_type=Double(optional=True),
                prefix="--log-mean-bias-standard-deviation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Standard deviation of log mean bias.  Default value: 0.1. "
                ),
            ),
            ToolInput(
                tag="mappingErrorRate",
                input_type=Double(optional=True),
                prefix="--mapping-error-rate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Typical mapping error rate. Default value: 0.01."
                ),
            ),
            ToolInput(
                tag="maxAdviIterFirstEpoch",
                input_type=Int(optional=True),
                prefix="--max-advi-iter-first-epoch",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum ADVI iterations in the first epoch.  Default value: 5000. "
                ),
            ),
            ToolInput(
                tag="maxAdviIterSubsequentEpochs",
                input_type=Int(optional=True),
                prefix="--max-advi-iter-subsequent-epochs",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum ADVI iterations in subsequent epochs.  Default value: 200. "
                ),
            ),
            ToolInput(
                tag="maxBiasFactors",
                input_type=Int(optional=True),
                prefix="--max-bias-factors",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum number of bias factors. Default value: 5."
                ),
            ),
            ToolInput(
                tag="maxCallingIters",
                input_type=Int(optional=True),
                prefix="--max-calling-iters",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum number of internal self-consistency iterations within each calling step. Default value: 10. "
                ),
            ),
            ToolInput(
                tag="maxCopyNumber",
                input_type=Int(optional=True),
                prefix="--max-copy-number",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Highest allowed copy-number state. Default value: 5."
                ),
            ),
            ToolInput(
                tag="maxTrainingEpochs",
                input_type=Boolean(optional=True),
                prefix="--max-training-epochs",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 50."),
            ),
            ToolInput(
                tag="minTrainingEpochs",
                input_type=Boolean(optional=True),
                prefix="--min-training-epochs",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 10."),
            ),
            ToolInput(
                tag="model",
                input_type=File(optional=True),
                prefix="--model",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input denoising-model directory. In COHORT mode, this argument is optional; if provided,a new model will be built using this input model to initialize. In CASE mode, this argument is required and the denoising model parameters are set to this input model.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="numGcBins",
                input_type=Int(optional=True),
                prefix="--num-gc-bins",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Number of bins used to represent the GC-bias curves. Default value: 20."
                ),
            ),
            ToolInput(
                tag="numThermalAdviIters",
                input_type=Int(optional=True),
                prefix="--num-thermal-advi-iters",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of thermal ADVI iterations (for DA-ADVI).  Default value: 2500. "
                ),
            ),
            ToolInput(
                tag="pActive",
                input_type=Double(optional=True),
                prefix="--p-active",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Prior probability of treating an interval as CNV-active (in a CNV-active domains, all copy-number states are equally likely to be called).  Default value: 0.01. "
                ),
            ),
            ToolInput(
                tag="pAlt",
                input_type=Double(optional=True),
                prefix="--p-alt",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Total prior probability of alternative copy-number states (the reference copy-number is set to the contig integer ploidy)  Default value: 1.0E-6. "
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
                tag="samplePsiScale",
                input_type=Double(optional=True),
                prefix="--sample-psi-scale",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Typical scale of sample-specific correction to the unexplained variance. Default value: 1.0E-4. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:05:38.353401"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:05:38.353402"),
            documentation="USAGE: GermlineCNVCaller [arguments]\nCalls copy-number variants in germline samples given their counts and the output of DetermineGermlineContigPloidy\nVersion:4.1.3.0\n",
        )
