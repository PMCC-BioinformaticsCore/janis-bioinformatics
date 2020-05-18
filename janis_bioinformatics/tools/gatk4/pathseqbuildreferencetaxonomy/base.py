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


class GatkPathSeqBuildReferenceTaxonomyBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "PathSeqBuildReferenceTaxonomy"

    def friendly_name(self) -> str:
        return "GATK4: PathSeqBuildReferenceTaxonomy"

    def tool(self) -> str:
        return "Gatk4PathSeqBuildReferenceTaxonomy"

    def inputs(self):
        return [
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Local path for the output file. By convention, the extension should be '.db' Required."
                ),
            ),
            ToolInput(
                tag="reference",
                input_type=String(optional=True),
                prefix="--reference",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference sequence file Required."),
            ),
            ToolInput(
                tag="taxDump",
                input_type=String(optional=True),
                prefix="--tax-dump",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-TD) Local path to taxonomy dump tarball (taxdump.tar.gz available at ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/)  Required. "
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
                tag="genbankCatalog",
                input_type=String(optional=True),
                prefix="--genbank-catalog",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-GC) Local path to Genbank catalog file (gbXXX.catalog.XXX.txt.gz at ftp://ftp.ncbi.nlm.nih.gov/genbank/catalog/)  Default value: null. "
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
                tag="minNonVirusContigLength",
                input_type=Int(optional=True),
                prefix="--min-non-virus-contig-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-min-non-virus-contig-length)  Minimum reference contig length for non-viruses  Default value: 0. "
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
                tag="refseqCatalog",
                input_type=String(optional=True),
                prefix="--refseq-catalog",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RC) Local path to catalog file (RefSeq-releaseXX.catalog.gz available at ftp://ftp.ncbi.nlm.nih.gov/refseq/release/release-catalog/)  Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:54:08.675582"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:54:08.675582"),
            documentation="USAGE: PathSeqBuildReferenceTaxonomy [arguments]\nBuild an annotated taxonomy datafile for a given microbe reference. The output file from this tool is required to run\nthe PathSeq pipeline.\nVersion:4.1.3.0\n",
        )
