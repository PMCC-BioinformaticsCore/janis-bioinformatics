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


class GatkCreateReadCountPanelOfNormalsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CreateReadCountPanelOfNormals"

    def friendly_name(self) -> str:
        return "GATK4: CreateReadCountPanelOfNormals"

    def tool(self) -> str:
        return "Gatk4CreateReadCountPanelOfNormals"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--input",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input TSV or HDF5 files containing integer read counts in genomic intervals for all samples in the panel of normals (output of CollectReadCounts).  Intervals must be identical and in the same order for all samples.  This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Output file for the panel of normals. Required."
                ),
            ),
            ToolInput(
                tag="annotatedIntervals",
                input_type=File(optional=True),
                prefix="--annotated-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input file containing annotations for GC content in genomic intervals (output of AnnotateIntervals).  If provided, explicit GC correction will be performed before performing SVD.  Intervals must be identical to and in the same order as those in the input read-counts files.  Default value: null. "
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
                tag="conf",
                input_type=String(optional=True),
                prefix="--conf",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Spark properties to set on the Spark context in the format <property>=<value> This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="doImputeZeros",
                input_type=Boolean(optional=True),
                prefix="--do-impute-zeros",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, impute zero-coverage values as the median of the non-zero values in the corresponding interval.  (This is applied after all filters.)  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="extremeOutlierTruncationPercentile",
                input_type=Double(optional=True),
                prefix="--extreme-outlier-truncation-percentile",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Fractional coverages normalized by genomic-interval medians that are below this percentile or above the complementary percentile are set to the corresponding percentile value.  (This is applied after all filters and imputation.)  Default value: 0.1. "
                ),
            ),
            ToolInput(
                tag="extremeSampleMedianPercentile",
                input_type=Double(optional=True),
                prefix="--extreme-sample-median-percentile",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Samples with a median (across genomic intervals) of fractional coverage normalized by genomic-interval medians  below this percentile or above the complementary percentile are filtered out.  (This is the fourth filter applied.)  Default value: 2.5. "
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
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="maximumZerosInIntervalPercentage",
                input_type=Double(optional=True),
                prefix="--maximum-zeros-in-interval-percentage",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Genomic intervals with a fraction of zero-coverage samples above this percentage are filtered out.  (This is the third filter applied.)  Default value: 5.0. "
                ),
            ),
            ToolInput(
                tag="maximumZerosInSamplePercentage",
                input_type=Double(optional=True),
                prefix="--maximum-zeros-in-sample-percentage",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Samples with a fraction of zero-coverage genomic intervals above this percentage are filtered out.  (This is the second filter applied.)  Default value: 5.0. "
                ),
            ),
            ToolInput(
                tag="minimumIntervalMedianPercentile",
                input_type=Double(optional=True),
                prefix="--minimum-interval-median-percentile",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Genomic intervals with a median (across samples) of fractional coverage (optionally corrected for GC bias) less than or equal to this percentile are filtered out.  (This is the first filter applied.)  Default value: 10.0. "
                ),
            ),
            ToolInput(
                tag="numberOfEigensamples",
                input_type=Int(optional=True),
                prefix="--number-of-eigensamples",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of eigensamples to use for truncated SVD and to store in the panel of normals.  The number of samples retained after filtering will be used instead if it is smaller than this.  Default value: 20. "
                ),
            ),
            ToolInput(
                tag="programName",
                input_type=String(optional=True),
                prefix="--program-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Name of the program running Default value: null."
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
                tag="sparkMaster",
                input_type=String(optional=True),
                prefix="--spark-master",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="URL of the Spark Master to submit jobs to when using the Spark pipeline runner. Default value: local[*]. "
                ),
            ),
            ToolInput(
                tag="sparkVerbosity",
                input_type=String(optional=True),
                prefix="--spark-verbosity",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Spark verbosity. Overrides --verbosity for Spark-generated logs only. Possible values: {ALL, DEBUG, INFO, WARN, ERROR, FATAL, OFF, TRACE}  Default value: null. "
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
                tag="maximumChunkSize",
                input_type=Int(optional=True),
                prefix="--maximum-chunk-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum HDF5 matrix chunk size. Large matrices written to HDF5 are chunked into equally sized subsets of rows (plus a subset containing the remainder, if necessary) to avoid a hard limit in Java HDF5 on the number of elements in a matrix.  However, since a single row is not allowed to be split across multiple chunks, the number of columns must be less than the maximum number of values in each chunk.  Decreasing this number will reduce heap usage when writing chunks.  Default value: 16777215. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:05:13.132067"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:05:13.132068"),
            documentation="USAGE: CreateReadCountPanelOfNormals [arguments]\nCreates a panel of normals for read-count denoising given the read counts for samples in the panel\nVersion:4.1.3.0\n",
        )
