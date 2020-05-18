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


class GatkDownsampleSamBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "DownsampleSam"

    def friendly_name(self) -> str:
        return "GATK4: DownsampleSam"

    def tool(self) -> str:
        return "Gatk4DownsampleSam"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) The input SAM or BAM file to downsample. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output, downsampled, SAM or BAM file to write. Required."
                ),
            ),
            ToolInput(
                tag="accuracy",
                input_type=Double(optional=True),
                prefix="--ACCURACY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-A) The accuracy that the downsampler should try to achieve if the selected strategy supports it. Note that accuracy is never guaranteed, but some strategies will attempt to provide accuracy within the requested bounds.Higher accuracy will generally require more memory.  Default value: 1.0E-4. "
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
                tag="compression_level",
                input_type=Int(optional=True),
                prefix="--COMPRESSION_LEVEL",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Compression level for all compressed files created (e.g. BAM and VCF). Default value: 2."
                ),
            ),
            ToolInput(
                tag="create_index",
                input_type=Boolean(optional=True),
                prefix="--CREATE_INDEX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create a BAM index when writing a coordinate-sorted BAM file. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="create_md5_file",
                input_type=Boolean(optional=True),
                prefix="--CREATE_MD5_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create an MD5 digest for any BAM or FASTQ files created. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="ga4gh_client_secrets",
                input_type=Boolean(optional=True),
                prefix="--GA4GH_CLIENT_SECRETS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: client_secrets.json."),
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
                tag="max_records_in_ram",
                input_type=Int(optional=True),
                prefix="--MAX_RECORDS_IN_RAM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When writing files that need to be sorted, this will specify the number of records stored in RAM before spilling to disk. Increasing this number reduces the number of file handles needed to sort the file, and increases the amount of RAM needed.  Default value: 500000. "
                ),
            ),
            ToolInput(
                tag="metrics_file",
                input_type=File(optional=True),
                prefix="--METRICS_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-M) The metrics file (of type QualityYieldMetrics) which will contain information about the downsampled file.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="probability",
                input_type=Double(optional=True),
                prefix="--PROBABILITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-P) The probability of keeping any individual read, between 0 and 1. Default value: 1.0."
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
                tag="random_seed",
                input_type=Int(optional=True),
                prefix="--RANDOM_SEED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) Random seed used for deterministic results. Setting to null will cause multiple invocations to produce different results.  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The reference sequence file. Default value: null."
                ),
            ),
            ToolInput(
                tag="strategy",
                input_type=Boolean(optional=True),
                prefix="--STRATEGY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-S) The downsampling strategy to use. See usage for discussion. Default value: ConstantMemory. Possible values: {HighAccuracy, ConstantMemory, Chained} "
                ),
            ),
            ToolInput(
                tag="tmp_dir",
                input_type=File(optional=True),
                prefix="--TMP_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="One or more directories with space available to be used by this program for temporary storage of working files  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="use_jdk_deflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_DEFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_deflater)  Use the JDK Deflater instead of the Intel Deflater for writing compressed output  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="use_jdk_inflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_INFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_inflater)  Use the JDK Inflater instead of the Intel Inflater for reading compressed input  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="validation_stringency",
                input_type=Boolean(optional=True),
                prefix="--VALIDATION_STRINGENCY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Validation stringency for all SAM files read by this program.  Setting stringency to SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default value: STRICT. Possible values: {STRICT, LENIENT, SILENT} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--VERBOSITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Control verbosity of logging. Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:56:47.465979"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:56:47.465981"),
            documentation="b'USAGE: DownsampleSam [arguments]\nDownsample a SAM or BAM file.This tool applies a downsampling algorithm to a SAM or BAM file to retain only a\n(deterministically random) subset of the reads. Reads from the same template (e.g. read-pairs, secondary and\nsupplementary reads) are all either kept or discarded as a unit, with the goal of retaining readsfrom PROBABILITY *\ninput templates. The results will contain approximately PROBABILITY * input reads, however for very small PROBABILITIES\nthis may not be the case.\nA number of different downsampling strategies are supported using the STRATEGY option:\nConstantMemory:\nDownsamples a stream or file of SAMRecords using a hash-projection strategy such that it can run in constant memory. The\ndownsampling is stochastic, and therefore the actual retained proportion will vary around the requested proportion. Due\nto working in fixed memory this strategy is good for large inputs, and due to the stochastic nature the accuracy of this\nstrategy is highest with a high number of output records, and diminishes at low output volumes.\nHighAccuracy:\nAttempts (but does not guarantee) to provide accuracy up to a specified limit. Accuracy is defined as emitting a\nproportion of reads as close to the requested proportion as possible. In order to do so this strategy requires memory\nthat is proportional to the number of template names in the incoming stream of reads, and will thus require large\namounts of memory when running on large input files.\nChained:\nAttempts to provide a compromise strategy that offers some of the advantages of both the ConstantMemory and HighAccuracy\nstrategies. Uses a ConstantMemory strategy to downsample the incoming stream to approximately the desired proportion,\nand then a HighAccuracy strategy to finish. Works in a single pass, and will provide accuracy close to (but often not as\ngood as) HighAccuracy while requiring memory proportional to the set of reads emitted from the ConstantMemory strategy\nto the HighAccuracy strategy. Works well when downsampling large inputs to small proportions (e.g. downsampling hundreds\nof millions of reads and retaining only 2%. Should be accurate 99.9% of the time when the input contains more than\n50,000 templates (read names). For smaller inputs, HighAccuracy is recommended instead.\n<h3>Usage examples:</h3>\n<h4>Downsample file, keeping about 10% of the reads</h4>\njava -jar picard.jar DownsampleSam \\\nI=input.bam \\\nO=downsampled.bam \\\nP=0.2\n<h3>Downsample file, keeping about 2% of the reads </h3>\njava -jar picard.jar DownsampleSam \\\nI=input.bam \\\nO=downsampled.bam \\\nSTRATEGY=Chained \\\nP=0.02 \\\nACCURACY=0.0001\n<h3>Downsample file, keeping about 0.001% of the reads (may require more memory)</h3>\njava -jar picard.jar DownsampleSam \\\nI=input.bam \\\nO=downsampled.bam \\\nSTRATEGY=HighAccuracy \\\nP=0.00001 \\\nACCURACY=0.0000001\nVersion:4.1.3.0\n",
        )
