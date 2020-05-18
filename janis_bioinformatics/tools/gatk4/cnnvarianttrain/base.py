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


class GatkCNNVariantTrainBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CNNVariantTrain"

    def friendly_name(self) -> str:
        return "GATK4: CNNVariantTrain"

    def tool(self) -> str:
        return "Gatk4CNNVariantTrain"

    def inputs(self):
        return [
            ToolInput(
                tag="inputTensorDir",
                input_type=String(optional=True),
                prefix="--input-tensor-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-input-tensor-dir)  Directory of training tensors to create.  Required. "
                ),
            ),
            ToolInput(
                tag="annotationShortcut",
                input_type=Boolean(optional=True),
                prefix="--annotation-shortcut",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-annotation-shortcut)  Shortcut connections on the annotation layers.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="annotationUnits",
                input_type=Int(optional=True),
                prefix="--annotation-units",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-annotation-units)  Number of units connected to the annotation input layer  Default value: 16. "
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
                tag="convBatchNormalize",
                input_type=Boolean(optional=True),
                prefix="--conv-batch-normalize",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-conv-batch-normalize)  Batch normalize convolution layers  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="convDropout",
                input_type=Float(optional=True),
                prefix="--conv-dropout",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-conv-dropout)  Dropout rate in convolution layers  Default value: 0.0. "
                ),
            ),
            ToolInput(
                tag="convHeight",
                input_type=Int(optional=True),
                prefix="--conv-height",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-conv-height)  Height of convolution kernels  Default value: 5. "
                ),
            ),
            ToolInput(
                tag="convLayers",
                input_type=Int(optional=True),
                prefix="--conv-layers",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-conv-layers)  List of number of filters to use in each convolutional layer  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="convWidth",
                input_type=Int(optional=True),
                prefix="--conv-width",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-conv-width)  Width of convolution kernels  Default value: 5. "
                ),
            ),
            ToolInput(
                tag="epochs",
                input_type=Int(optional=True),
                prefix="--epochs",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-epochs) Maximum number of training epochs. Default value: 10."
                ),
            ),
            ToolInput(
                tag="fcBatchNormalize",
                input_type=Boolean(optional=True),
                prefix="--fc-batch-normalize",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-fc-batch-normalize)  Batch normalize fully-connected layers  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="fcDropout",
                input_type=Boolean(optional=True),
                prefix="--fc-dropout",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-fc-dropout) Default value: 0.0."),
            ),
            ToolInput(
                tag="fcLayers",
                input_type=String(optional=True),
                prefix="--fc-layers",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-fc-layers) This argument may be specified 0 or more times. Default value: null. "
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
                tag="imageDir",
                input_type=Boolean(optional=True),
                prefix="--image-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-image-dir) Default value: null."),
            ),
            ToolInput(
                tag="modelName",
                input_type=String(optional=True),
                prefix="--model-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-model-name)  Name of the model to be trained.  Default value: variant_filter_model. "
                ),
            ),
            ToolInput(
                tag="outputDir",
                input_type=String(optional=True),
                prefix="--output-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-output-dir)  Directory where models will be saved, defaults to current working directory.  Default value: ./. "
                ),
            ),
            ToolInput(
                tag="padding",
                input_type=String(optional=True),
                prefix="--padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-padding) Padding for convolution layers, valid or same Default value: valid."
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
                tag="spatialDropout",
                input_type=Boolean(optional=True),
                prefix="--spatial-dropout",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-spatial-dropout)  Spatial dropout on convolution layers  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="tensorType",
                input_type=Boolean(optional=True),
                prefix="--tensor-type",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-tensor-type)  Type of tensors to use as input reference for 1D reference tensors and read_tensor for 2D tensors.  Default value: reference. Possible values: { reference ( 1 Hot encoding of a reference sequence. ) read_tensor (Read tensor are 3D tensors spanning aligned reads, sites and channels. The maximum number of reads is a hyper-parameter typically set to 128. There are 15 channels in the read tensor. They correspond to the reference sequence data (4), read sequence data (4), insertions and deletions (2) read flags (4) and mapping quality (1).) } "
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
                tag="trainingSteps",
                input_type=Int(optional=True),
                prefix="--training-steps",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-training-steps)  Number of training steps per epoch.  Default value: 10. "
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
                tag="validationSteps",
                input_type=Int(optional=True),
                prefix="--validation-steps",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-validation-steps)  Number of validation steps per epoch.  Default value: 2. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:05:52.849152"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:05:52.849153"),
            documentation="**EXPERIMENTAL FEATURE - USE AT YOUR OWN RISK**\nUSAGE: CNNVariantTrain [arguments]\nTrain a CNN model for filtering variants\nVersion:4.1.3.0\n",
        )
