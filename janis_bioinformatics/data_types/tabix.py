from janis_unix.data_types.gunzipped import Gunzipped


class FileTabix(Gunzipped):
    @staticmethod
    def secondary_files():
        return [".tbi"]
