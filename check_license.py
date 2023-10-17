import json
import os

class CheckLicense:

    ALLOWED_LICENSES = os.environ.get("ALLOWED_LICENSES").split(", ")
    def __init__(self, file):
        self.file = file

    def read_file(self):
        data = []
        print(self.file)
        with open(self.file, "r") as file:
            data = json.load(file)

        return self._check_license(data)

    def _check_license(self, data):
        bad_dependency = {}
        bad_dependency["file"] = self.file
        bad_dependency["dep"] = []
        for item in data:
            for license in item["licenses"]:
                if license not in self.ALLOWED_LICENSES:
                    bad_dependency["dep"].append(item)

        if len(bad_dependency) > 0:
            print(bad_dependency)
            return bad_dependency
