import json


class CheckLicense:

    ALLOWED_LICENSES = ["MIT License", "BSD License"]

    def __init__(self, file):
        self.file = file

    def read_file(self):
        data = []
        print(self.file)
        with open(self.file, "r") as file:
            data = json.load(file)

        return self._check_license(data)

    def _check_license(self, data):
        bad_dependency = []
        # bad_dependency["file"] = self.file

        for item in data:
            for license in item["licenses"]:
                if license not in self.ALLOWED_LICENSES:
                    bad_dependency.append(item)

        if len(bad_dependency) > 0:
            return bad_dependency
