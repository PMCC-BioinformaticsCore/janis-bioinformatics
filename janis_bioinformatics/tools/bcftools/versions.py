class BcfTools_1_5:
    def container(self):
        # Todo: Create a docker container with 1_9
        return "biocontainers/bcftools:v1.5_cv2"

    def version(self):
        return "v1.5"


class BcfTools_1_9:
    def container(self):
        return "biocontainers/bcftools:v1.9-1-deb_cv1"

    def version(self):
        return "v1.9"


class BcfTools_1_12:
    def container(self):
        return "quay.io/biocontainers/bcftools:1.12--h45bccc9_1"

    def version(self):
        return "v1.12"
