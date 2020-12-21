from datetime import datetime
from abc import ABC

from janis_core import ToolInput, Boolean, Filename, String, Int, ToolMetadata
from .base import VepBase_98_3


class VepDatabaseBase_98_3(VepBase_98_3, ABC):
    def tool(self) -> str:
        return "vep_database"

    def friendly_name(self):
        return "Vep (Database)"

    def inputs(self):
        return [
            *super().inputs(),  # cache options
            ToolInput(
                "database",
                Boolean(optional=True),
                prefix="--database",
                doc="Enable VEP to use local or remote databases.",
            ),
            ToolInput(
                "host",
                String(optional=True),
                prefix="--host",
                doc="Manually define the database host to connect to. Users in the US may find connection and transfer "
                'speeds quicker using our East coast mirror, useastdb.ensembl.org. Default = "ensembldb.ensembl.org"',
            ),
            ToolInput(
                "user",
                String(optional=True),
                prefix="--user",
                doc='(-u) Manually define the database username. Default = "anonymous"',
            ),
            ToolInput(
                "password",
                String(optional=True),
                prefix="--password",
                doc="(--pass) Manually define the database password. Not used by default",
            ),
            ToolInput(
                "port",
                Int(optional=True),
                prefix="--port",
                doc="Manually define the database port. Default = 5306",
            ),
            ToolInput(
                "genomes",
                Boolean(optional=True),
                prefix="--genomes",
                doc="Override the default connection settings with those for the Ensembl Genomes public MySQL server. "
                "Required when using any of the Ensembl Genomes species. Not used by default",
            ),
            ToolInput(
                "isMultispecies",
                Boolean(optional=True),
                prefix="--is_multispecies",
                doc="Some of the Ensembl Genomes databases (mainly bacteria and protists) are composed of a collection "
                "of close species. It updates the database connection settings (i.e. the database name) "
                "if the value is set to 1. Default: 0",
            ),
            ToolInput(
                "lrg",
                Boolean(optional=True),
                prefix="--lrg",
                doc="Map input variants to LRG coordinates (or to chromosome coordinates if given in LRG coordinates), "
                "and provide consequences on both LRG and chromosomal transcripts. Not used by default",
            ),
            ToolInput(
                "dbVersion",
                String(optional=True),
                prefix="--db_version",
                doc="Force VEP to connect to a specific version of the Ensembl databases. Not recommended as there "
                "may be conflicts between software and database versions. Not used by default",
            ),
            ToolInput(
                "registry",
                Filename(),
                prefix="--registry",
                doc="Defining a registry file overwrites other connection settings and uses those found in the "
                "specified registry file to connect. Not used by default",
            ),
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime(2020, 2, 25),
            dateUpdated=datetime(2020, 5, 7),
            documentation="",
        )
