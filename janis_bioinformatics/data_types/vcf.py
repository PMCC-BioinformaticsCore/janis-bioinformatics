import gzip
import hashlib
import re
from abc import ABC

from janis_core import File
from janis_unix import Gunzipped

from janis_bioinformatics.data_types.tabix import FileTabix
from janis_core.tool.test_classes import (
    TTestPreprocessor,
    TTestExpectedOutput,
    TTestCase,
)
import operator


class Vcf(File):
    def __init__(self, optional=False):
        super().__init__(optional=optional, extension=".vcf")

    @staticmethod
    def name():
        return "VCF"

    def doc(self):
        return """
    Variant Call Format:

    The Variant Call Format (VCF) specifies the format of a text file 
    used in bioinformatics for storing gene sequence variations. 

    Documentation: https://samtools.github.io/hts-specs/VCFv4.3.pdf
    """.strip()

    @classmethod
    def md5(cls, file_path: str):
        with open(file_path, "r") as f:
            meaningful_content = False
            hash_md5 = hashlib.md5()
            while True:
                line = f.readline()
                if not line:
                    break
                if re.match("^#CHROM", line):
                    meaningful_content = True
                if not meaningful_content:
                    continue
                hash_md5.update(line.encode())
        return hash_md5.hexdigest()

    @classmethod
    def basic_test(cls, tag, md5_value):
        return [
            TTestExpectedOutput(
                tag=tag,
                preprocessor=Vcf.md5,
                operator=operator.eq,
                expected_value=md5_value,
            ),
        ]


class VcfIdx(Vcf):
    @staticmethod
    def name():
        return "IndexedVCF"

    @staticmethod
    def secondary_files():
        return [".idx"]

    @classmethod
    def basic_test(cls, tag, vcf_md5, idx_md5):
        return Vcf.basic_test(tag, vcf_md5) + [
            TTestExpectedOutput(
                tag=tag,
                suffix_secondary_file=".idx",
                preprocessor=TTestPreprocessor.FileMd5,
                operator=operator.eq,
                expected_value=idx_md5,
            ),
        ]


class CompressedVcf(Gunzipped):
    def __init__(self, optional=False):
        super().__init__(inner_type=Vcf, optional=optional, extension=".vcf.gz")

    @staticmethod
    def name():
        return "CompressedVCF"

    def doc(self):
        return ".vcf.gz"

    @classmethod
    def md5(cls, file_path: str):
        with gzip.open(file_path, "rt") as f:
            meaningful_content = False
            hash_md5 = hashlib.md5()
            while True:
                line = f.readline()
                if not line:
                    break
                if re.match("^#CHROM", line):
                    meaningful_content = True
                if not meaningful_content:
                    continue
                hash_md5.update(line.encode())
        return hash_md5.hexdigest()

    @classmethod
    def basic_test(cls, tag, md5_value):
        return [
            TTestExpectedOutput(
                tag=tag,
                preprocessor=CompressedVcf.md5,
                operator=operator.eq,
                expected_value=md5_value,
            ),
        ]


class VcfTabix(CompressedVcf, FileTabix):
    @staticmethod
    def name():
        return "CompressedIndexedVCF"

    def doc(self):
        return ".vcf.gz with .vcf.gz.tbi file"

    @classmethod
    def basic_test(cls, tag, vcf_md5, tbi_size):
        return CompressedVcf.basic_test(tag, vcf_md5) + [
            TTestExpectedOutput(
                tag=tag,
                suffix_secondary_file=".tbi",
                preprocessor=TTestPreprocessor.FileSize,
                operator=operator.gt,
                expected_value=tbi_size,
            ),
        ]


# class GVCF(Vcf):
#     @staticmethod
#     def name():
#         return "gVCF"
#
#     def doc(self):
#         return """
# Section 5.5: Representing unspecified alleles and REF only blocks (gVCF)
# Documentation: https://samtools.github.io/hts-specs/VCFv4.3.pdf
#         """
