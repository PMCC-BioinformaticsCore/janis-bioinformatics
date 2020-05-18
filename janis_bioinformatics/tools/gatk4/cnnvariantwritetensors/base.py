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


class GatkCNNVariantWriteTensorsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CNNVariantWriteTensors"

    def friendly_name(self) -> str:
        return "GATK4: CNNVariantWriteTensors"

    def tool(self) -> str:
        return "Gatk4CNNVariantWriteTensors"

    def inputs(self):
        return [
            ToolInput(
                tag="outputTensorDir",
                input_type=String(optional=True),
                prefix="--output-tensor-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-output-tensor-dir)  Directory of training tensors. Subdivided into train, valid and test sets.  Required. "
                ),
            ),
            ToolInput(
                tag="reference",
                input_type=String(optional=True),
                prefix="--reference",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference fasta file. Required."),
            ),
            ToolInput(
                tag="truthBed",
                input_type=Boolean(optional=True),
                prefix="--truth-bed",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-truth-bed) Required."),
            ),
            ToolInput(
                tag="truthVcf",
                input_type=Boolean(optional=True),
                prefix="--truth-vcf",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-truth-vcf) Required."),
            ),
            ToolInput(
                tag="variant",
                input_type=String(optional=True),
                prefix="--variant",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-V) Input VCF file Required."),
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
                tag="bamFile",
                input_type=String(optional=True),
                prefix="--bam-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-bam-file) BAM or BAMout file to use for read data when generating 2D tensors. Default value: ."
                ),
            ),
            ToolInput(
                tag="downsampleIndels",
                input_type=Float(optional=True),
                prefix="--downsample-indels",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-downsample-indels)  Fraction of INDELs to write tensors for.  Default value: 0.5. "
                ),
            ),
            ToolInput(
                tag="downsampleSnps",
                input_type=Float(optional=True),
                prefix="--downsample-snps",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-downsample-snps)  Fraction of SNPs to write tensors for.  Default value: 0.05. "
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
                tag="maxTensors",
                input_type=Int(optional=True),
                prefix="--max-tensors",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-max-tensors)  Maximum number of tensors to write.  Default value: 1000000. "
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
                tag="tensorType",
                input_type=Boolean(optional=True),
                prefix="--tensor-type",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-tensor-type)  Name of the tensors to generate.  Default value: reference. Possible values: { reference ( 1 Hot encoding of a reference sequence. ) read_tensor (Read tensor are 3D tensors spanning aligned reads, sites and channels. The maximum number of reads is a hyper-parameter typically set to 128. There are 15 channels in the read tensor. They correspond to the reference sequence data (4), read sequence data (4), insertions and deletions (2) read flags (4) and mapping quality (1).) } "
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
                tag="annotationSet",
                input_type=String(optional=True),
                prefix="--annotation-set",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-annotation-set)  Which set of annotations to use.  Default value: best_practices. "
                ),
            ),
            ToolInput(
                tag="channelsLast",
                input_type=Boolean(optional=True),
                prefix="--channels-last",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-channels-last)  Store the channels in the last axis of tensors, tensorflow->true, theano->false  Default value: true. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:06:00.137783"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:06:00.137784"),
            documentation="**EXPERIMENTAL FEATURE - USE AT YOUR OWN RISK**\nUSAGE: CNNVariantWriteTensors [arguments]\nWrite variant tensors for training a CNN to filter variants\nVersion:4.1.3.0\n",
        )
