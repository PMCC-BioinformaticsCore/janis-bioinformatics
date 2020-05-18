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


class GatkPlotModeledSegmentsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "PlotModeledSegments"

    def friendly_name(self) -> str:
        return "GATK4: PlotModeledSegments"

    def tool(self) -> str:
        return "Gatk4PlotModeledSegments"

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
                tag="segments",
                input_type=File(optional=True),
                prefix="--segments",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input file containing modeled segments (output of ModelSegments). Required."
                ),
            ),
            ToolInput(
                tag="sequenceDictionary",
                input_type=File(optional=True),
                prefix="--sequence-dictionary",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-sequence-dictionary)  File containing a sequence dictionary, which specifies the contigs to be plotted and their relative lengths. The sequence dictionary must be a subset of those contained in other input files. Contigs will be plotted in the order given. Contig names should not include the string 'CONTIG_DELIMITER'. The tool only considers contigs in the given dictionary for plotting, and data for contigs absent in the dictionary generate only a warning. In other words, you may modify a reference dictionary for use with this tool to include only contigs for which plotting is desired, and sort the contigs to the order in which the plots should display the contigs.  Required. "
                ),
            ),
            ToolInput(
                tag="allelicCounts",
                input_type=File(optional=True),
                prefix="--allelic-counts",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input file containing allelic counts at heterozygous sites (.hets.tsv output of ModelSegments).  Default value: null. "
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
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="minimumContigLength",
                input_type=Int(optional=True),
                prefix="--minimum-contig-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Threshold length (in bp) for contigs to be plotted. Contigs with lengths less than this threshold will not be plotted. This can be used to filter out mitochondrial contigs, unlocalized contigs, etc.  Default value: 1000000. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:06:10.492726"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:06:10.492727"),
            documentation="USAGE: PlotModeledSegments [arguments]\nCreates plots of denoised and segmented copy-ratio and minor-allele-fraction estimates\nVersion:4.1.3.0\n",
        )
