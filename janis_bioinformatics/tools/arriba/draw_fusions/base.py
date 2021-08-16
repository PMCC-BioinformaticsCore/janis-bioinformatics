from abc import ABC
from datetime import datetime

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool
from janis_unix import Csv, Tsv

from janis_bioinformatics.data_types import BamBai
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
    Array,
)
from janis_bioinformatics.tools.arriba.base import ArribaBase


class ArribaDrawFusionsBase(ArribaBase, ABC):
    @classmethod
    def arriba_command(self):
        return "/usr/local/bin/draw_fusions.R"

    def friendly_name(self) -> str:
        return "Arriba: DrawFusions"

    def tool(self) -> str:
        return "ArribaDrawFusions"

    def inputs(self):
        return [
            ToolInput(
                tag="annotation",
                input_type=File(),
                prefix="--annotation=",
                separate_value_from_prefix=False,
                doc="exonsFile",
            ),
            ToolInput(
                tag="fusions",
                input_type=File(),
                prefix="--fusions=",
                separate_value_from_prefix=False,
                doc="fusionsFile",
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(extension=".pdf"),
                prefix="--output=",
                separate_value_from_prefix=False,
                doc="outputFile",
            ),
            ToolInput(
                tag="alignments",
                input_type=BamBai(optional=True),
                prefix="--alignments=",
                separate_value_from_prefix=False,
                doc="alignmentsFile",
            ),
            ToolInput(
                tag="cytobands",
                input_type=File(optional=True),
                prefix="--cytobands=",
                separate_value_from_prefix=False,
                doc="cytobandsFile",
            ),
            ToolInput(
                tag="minConfidenceForCircosPlot",
                input_type=String(optional=True),
                prefix="--minConfidenceForCircosPlot=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="proteinDomains",
                input_type=File(optional=True),
                prefix="--proteinDomains=",
                separate_value_from_prefix=False,
                doc="proteinDomainsFile",
            ),
            ToolInput(
                tag="squishIntrons",
                input_type=Boolean(optional=True),
                prefix="--squishIntrons=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="printExonLabels",
                input_type=Boolean(optional=True),
                prefix="--printExonLabels=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="renderThreeDEffect",
                input_type=Boolean(optional=True),
                prefix="--render3dEffect=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="pdfWidth",
                input_type=Float(optional=True),
                prefix="--pdfWidth=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="pdfHeight",
                input_type=Float(optional=True),
                prefix="--pdfHeight=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="color_one",
                input_type=String(optional=True),
                prefix="--color1=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="color_two",
                input_type=String(optional=True),
                prefix="--color2=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="mergeDomainsOverlappingBy",
                input_type=Float(optional=True),
                prefix="--mergeDomainsOverlappingBy=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="optimizeDomainColors",
                input_type=Boolean(optional=True),
                prefix="--optimizeDomainColors=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="fontSize",
                input_type=Int(optional=True),
                prefix="--fontSize=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="showIntergenicVicinity",
                input_type=Int(optional=True),
                prefix="--showIntergenicVicinity=",
                separate_value_from_prefix=False,
                doc="",
            ),
            ToolInput(
                tag="transcriptSelection",
                input_type=String(optional=True),
                prefix="--transcriptSelection=",
                separate_value_from_prefix=False,
                doc="",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", File, selector=InputSelector("outputFilename"))]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2021, 3, 15),
            dateUpdated=datetime(2021, 3, 15),
            documentation="""
Arriba comes with an R script draw_fusions.R that renders publication-quality 
visualizations of the transcripts involved in predicted fusions. It generates 
a PDF file with one page for each predicted fusion. Each page depicts the 
fusion partners, their orientation, the retained exons in the fusion 
transcript, statistics about the number of supporting reads, and - if the 
column fusion_transcript has a value - an excerpt of the sequence around the 
breakpoint.
""",
        )
