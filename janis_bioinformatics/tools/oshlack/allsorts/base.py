from abc import ABC
from datetime import datetime
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
from janis_unix import Csv


class AllSortsBase(CommandTool, ABC):
    def friendly_name(self) -> str:
        return "Allsorts"

    def tool_provider(self):
        return "oshlack"

    def tool(self) -> str:
        return "Allsorts"

    def base_command(self):
        return ["ALLSorts"]

    def inputs(self):
        return [
            # ToolInput(
            #     tag="help",
            #     input_type=Boolean(optional=True),
            #     prefix="--help",
            #     separate_value_from_prefix=True,
            #     doc=InputDocumentation(doc="(-h) show this help message and exit"),
            # ),
            ToolInput(
                tag="samples",
                input_type=Csv(),
                prefix="-samples",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-s)  Path to samples (rows) x genes (columns) csv file representing a raw counts matrix. Note: hg19 only supported currently, use other references at own risk."
                ),
            ),
            ToolInput(
                tag="labels",
                input_type=Csv(),
                prefix="-labels",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-l)  (Optional) Path to samples true labels. CSV with samples (rows) x [sample id, label] (cols). This will enable re-labelling mode. Note: labels must reflect naming conventions used within this tool. View the ALLSorts GitHub Wiki for further details."
                ),
            ),
            ToolInput(
                tag="destination",
                input_type=String(optional=True),
                prefix="-destination",
                default=".",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-d)  Path to where you want the final report to be saved."
                ),
            ),
            # ToolInput(
            #     tag="test",
            #     input_type=Boolean(optional=True),
            #     prefix="-test",
            #     separate_value_from_prefix=True,
            #     doc=InputDocumentation(
            #         doc="(-t) Test will run a simple logistic regression."
            #     ),
            # ),
            # ToolInput(
            #     tag="train",
            #     input_type=Boolean(optional=True),
            #     prefix="-train",
            #     separate_value_from_prefix=True,
            #     doc=InputDocumentation(
            #         doc="Train a new model. -labels/-l and -samples/-s must be set."
            #     ),
            # ),
            # ToolInput(
            #     tag="model_dir",
            #     input_type=Boolean(optional=True),
            #     prefix="-model_dir",
            #     separate_value_from_prefix=True,
            #     doc=InputDocumentation(
            #         doc="Directory for a new model. -train -t flag must be set."
            #     ),
            # ),
            # ToolInput(
            #     tag="njobs",
            #     input_type=Boolean(optional=True),
            #     prefix="-njobs",
            #     separate_value_from_prefix=True,
            #     doc=InputDocumentation(
            #         doc="(-j)  (int, default=1) Will set n_jobs for all Sklearn estimators/transformers."
            #     ),
            # ),
            # ToolInput(
            #     tag="cv",
            #     input_type=Boolean(optional=True),
            #     prefix="-cv",
            #     separate_value_from_prefix=True,
            #     doc=InputDocumentation(
            #         doc="(int, default=3) If training, how many folds in the cross validation?"
            #     ),
            # ),
            ToolInput(
                tag="verbose",
                input_type=Boolean(optional=True),
                prefix="-verbose",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-v) (flag, default=False) Verbose. Print stage progress."
                ),
            ),
            ToolInput(
                tag="comparison",
                input_type=Boolean(optional=True),
                prefix="-comparison",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Rebuild comparisons for labelled visualisations."
                ),
            ),
            ToolInput(
                tag="force",
                input_type=Boolean(optional=True),
                prefix="-force",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-f) (flag, default=False) Force. Bypass warnings without user confirmation."
                ),
            ),
            ToolInput(
                tag="parents",
                input_type=Boolean(optional=True),
                prefix="-parents",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-p) Include parent meta-subtypes in predictions. Note: This may remove previously unclassified samples."
                ),
            ),
        ]

    def outputs(self):
        return [
            ToolOutput("out_predictions", Csv, selector="predictions.csv"),
            ToolOutput("out_probabilities", Csv, selector="probabilities.csv"),
            ToolOutput("out_distributions", File, selector="distributions.png"),
            ToolOutput("out_waterfalls", File, selector="waterfalls.png"),
        ]

    def metadata(self):
        return ToolMetadata(
            contributors=[],
            dateCreated=datetime(2020, 9, 2),
            dateUpdated=datetime(2020, 9, 2),
            documentation="usage: ALLSorts [-h] -samples SAMPLES [-labels LABELS]\n                [-destination DESTINATION] [-test] [-train]\n                [-model_dir MODEL_DIR] [-njobs NJOBS] [-cv CV] [-verbose]\n                [-comparison] [-force] [-parents]\nALLSorts CLI\n",
        )
