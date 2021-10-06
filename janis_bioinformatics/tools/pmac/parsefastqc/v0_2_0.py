"""
Each modification of this tool should duplicate this code
"""
import operator
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

from janis_core import PythonTool, File, Array, ToolMetadata
from janis_core.tool.test_classes import (
    TTestCase,
    TTestExpectedOutput,
    TTestPreprocessor,
)
from janis_core.tool.tool import TOutput

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsPythonTool
from janis_bioinformatics.tools import BioinformaticsTool


class ParseFastqcAdaptors(BioinformaticsPythonTool):
    @staticmethod
    def code_block(
        fastqc_datafiles: List[File], cutadapt_adaptors_lookup: Optional[File]
    ):
        """

        :param fastqc_datafiles:

        :param cutadapt_adaptors_lookup: Specifies a file which contains the list of adapter sequences which will
            be explicity searched against the library. The file must contain sets of named adapters in
            the form name[tab]sequence. Lines prefixed with a hash will be ignored.
        :return:
        """
        if not cutadapt_adaptors_lookup:
            return {"adaptor_sequences": []}

        import mmap, re, csv
        from io import StringIO
        from sys import stderr

        def get_overrepresented_text(f):
            """
            Get the table "Overrepresented sequences" within the fastqc_data.txt
            """
            adapt_section_query = (
                br"(?s)>>Overrepresented sequences\t\S+\n(.*?)>>END_MODULE"
            )
            # fastqc_datafile could be fairly large, so we'll use mmap, and then
            with open(f) as f, mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as fp:
                overrepresented_sequences_match = re.search(adapt_section_query, fp)
                if overrepresented_sequences_match is None:
                    raise Exception(
                        f"Couldn't find query ('{adapt_section_query.decode('utf8')}') in {fastqc_datafiles}"
                    )

                return overrepresented_sequences_match.groups()[0].decode("utf8")

        def parse_tsv_table(tbl: str, skip_headers):
            """
            Parse a TSV table from a string using csvreader
            """

            rd = csv.reader(StringIO(tbl), delimiter="\t", quotechar='"')
            ret = list(rd)
            if len(ret) == 0:
                return ret
            if skip_headers:
                ret.pop(0)  # discard headers
            return ret

        def get_cutadapt_map():
            """
            Helper method to parse the file 'cutadapt_adaptors_lookup' with
            format: 'name[tab]sequence' into the dictionary: '{ sequence: name }'
            """
            cutadapt_map = {}
            with open(cutadapt_adaptors_lookup) as fp:
                for row in fp:
                    st = row.strip()
                    if not st or st.startswith("#"):
                        continue

                    # In reality, the format is $name[\t+]$seqence (more than one tab)
                    # so we'll just split on a tab, and remove all the empty elements.
                    split = [f for f in st.split("\t") if bool(f) and len(f) > 0]

                    # Invalid format for line, so skip it.
                    if len(split) != 2:
                        print(
                            f"Skipping cutadapt line '{st}' as irregular elements ({len(split)})",
                            file=stderr,
                        )
                        continue

                    # reverse the order from name[tab]sequence to { sequence: tab }
                    cutadapt_map[split[0]] = split[1]
            return cutadapt_map

        # Start doing the work
        # Look up overrepresented sequences
        overrepresented_sequences = set()
        for fastqcfile in fastqc_datafiles:
            text = get_overrepresented_text(fastqcfile)
            overrepresented_sequences = overrepresented_sequences.union(
                set(a[0] for a in parse_tsv_table(text, skip_headers=True))
            )

        # Look up adaptor sequences
        adaptor_sequences = []
        adaptor_status = False
        for fastqcfile in fastqc_datafiles:
            for line in open(fastqcfile, "r"):
                if line.startswith(">>Adapter Content"):
                    adaptor_qc_line = line
                    adaptor_status = True
                elif adaptor_status == False:
                    continue
                elif adaptor_status == True and not line.startswith(">>END_MODULE"):
                    if line.startswith("#Position"):
                        adaptor_list = line.strip("\n").split("\t")
                    else:
                        adaptor_percentage = line.strip("\n").split("\t")

            # Parse adaptor id if adaptor qc fails
            if "fail" in adaptor_qc_line:
                cutadapt_map = get_cutadapt_map()
                for (aid, percentage) in zip(adaptor_list[1:], adaptor_percentage[1:]):
                    if float(percentage) >= 10:
                        if aid in cutadapt_map:
                            sequence = cutadapt_map.get(aid)
                            print(
                                f"Identified adaptor '{aid}' sequence '{sequence}' in lookup",
                                file=stderr,
                            )
                            adaptor_sequences.append(sequence)
                        else:
                            print(
                                f"Couldn't find a corresponding sequence for '{aid}' in lookup map",
                                file=stderr,
                            )
            else:
                pass

        return {
            "adaptor_sequences": list(overrepresented_sequences) + adaptor_sequences
        }

    def outputs(self) -> List[TOutput]:
        return [TOutput("adaptor_sequences", Array(str))]

    def id(self) -> str:
        return "ParseFastqcAdaptors"

    def friendly_name(self):
        return "Parse FastQC Adaptors"

    def version(self):
        return "v0.2.0"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        self.metadata.documentation = (
            "Parse overrepresented region and lookup in Cutadapt table"
        )
        self.metadata.contributors = ["Michael Franklin", "Jiaan Yu"]
        self.metadata.dateCreated = datetime(2020, 1, 7)
        self.metadata.dateUpdated = datetime(2021, 10, 6)
        self.metadata.version = "0.1.0"

    def tests(self):
        remote_dir = "https://swift.rc.nectar.org.au/v1/AUTH_4df6e734a509497692be237549bbe9af/janis-test-data/bioinformatics/wgsgermline_data"
        return [
            TTestCase(
                name="basic",
                input={
                    "fastqc_datafiles": [
                        f"{remote_dir}/NA12878-BRCA1.fastqc_data.txt",
                    ],
                    "cutadapt_adaptors_lookup": f"{remote_dir}/contaminant_list.txt",
                },
                output=[],
            ),
        ]
