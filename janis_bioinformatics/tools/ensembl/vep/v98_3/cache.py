from datetime import datetime
from abc import ABC

from janis_core import ToolInput, Boolean, Directory, Int, ToolMetadata
from janis_bioinformatics.data_types import FastaWithDict
from .base import VepBase_98_3


class VepCacheBase_98_3(VepBase_98_3, ABC):
    def tool(self) -> str:
        return "vep_cache"

    def friendly_name(self):
        return "Vep (Cache)"

    def inputs(self):
        return [
            *super().inputs(),  # cache options
            ToolInput(
                "cache",
                Boolean(optional=True),
                default=True,
                prefix="--cache",
                doc="Enables use of the cache. Add --refseq or --merged to use the refseq or merged cache.",
            ),
            ToolInput(
                "cacheDir",
                Directory(optional=True),
                prefix="--dir",
                doc='Specify the base cache/plugin directory to use. Default = "$HOME/.vep/"',
            ),
            ToolInput(
                "dirCache",
                Directory(optional=True),
                prefix="--dir_cache",
                doc='Specify the cache directory to use. Default = "$HOME/.vep/"',
            ),
            ToolInput(
                "dirPlugins",
                Directory(optional=True),
                prefix="--dir_plugins",
                doc='Specify the plugin directory to use. Default = "$HOME/.vep/"',
            ),
            ToolInput(
                "offline",
                Boolean(optional=True),
                default=True,
                prefix="--offline",
                doc="Enable offline mode. No database connections will be made, and a cache file or GFF/GTF file is "
                "required for annotation. Add --refseq to use the refseq cache (if installed). Not used by default",
            ),
            ToolInput(
                "fasta",
                FastaWithDict(optional=True),
                prefix="--fasta",
                doc="(--fa) Specify a FASTA file or a directory containing FASTA files to use to look up reference "
                "sequence. The first time you run VEP with this parameter an index will be built which can take a "
                "few minutes. This is required if fetching HGVS annotations (--hgvs) or checking reference "
                "sequences (--check_ref) in offline mode (--offline), and optional with some performance increase "
                "in cache mode (--cache). See documentation for more details. Not used by default",
            ),
            ToolInput(
                "refseq",
                Boolean(optional=True),
                prefix="--refseq",
                doc="Specify this option if you have installed the RefSeq cache in order for VEP to pick up the "
                "alternate cache directory. This cache contains transcript objects corresponding to RefSeq "
                "transcripts. Consequence output will be given relative to these transcripts in place of the "
                "default Ensembl transcripts (see documentation)",
            ),
            ToolInput(
                "merged",
                Boolean(optional=True),
                prefix="--merged",
                doc="Use the merged Ensembl and RefSeq cache. Consequences are flagged "
                "with the SOURCE of each transcript used.",
            ),
            ToolInput(
                "cacheVersion",
                Boolean(optional=True),
                prefix="--cache_version",
                doc="Use a different cache version than the assumed default (the VEP version). This should be used "
                "with Ensembl Genomes caches since their version numbers do not match Ensembl versions. "
                "For example, the VEP/Ensembl version may be 88 and the Ensembl Genomes version 35. "
                "Not used by default",
            ),
            ToolInput(
                "showCacheInfo",
                Boolean(optional=True),
                prefix="--show_cache_info",
                doc="Show source version information for selected cache and quit",
            ),
            ToolInput(
                "bufferSize",
                Int(optional=True),
                prefix="--buffer_size",
                doc="Sets the internal buffer size, corresponding to the number of variants that are read in to memory "
                "simultaneously. Set this lower to use less memory at the expense of longer run time, and higher "
                "to use more memory with a faster run time. Default = 5000",
            ),
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime(2020, 2, 25),
            dateUpdated=datetime(2020, 5, 7),
            documentation="",
        )
