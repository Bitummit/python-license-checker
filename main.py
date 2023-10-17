import os
from file_finder import find
from check_license import CheckLicense


def check_files(requirement_files):

    for file in requirement_files:

        file_name = file.split('/')[-1].split('.')[0]
        # Install requirements and write licenses to json file
        os.system(f'pip install -r {file}')
        os.system('pip install pip-licenses')
        os.system(f'pip-licenses --format=json-license-finder --output-file={file_name}.json --ignore-packages pkg_resources')

        lic = CheckLicense(f"{file_name}.json")
        result = lic.read_file()
        report.append(result) if result else print(f"----------No bad dependencies found for {file_name}-----------")

        # clear venv for next file
        os.system(f'pip freeze > {file}')
        os.system(f'pip uninstall -y -r {file}')


def make_report(report):
    if report:
        for item in report:
            print('<-------------------', item['file'], '--------------------->')
            print(*item['dep'], sep='\n')

            print('<----------------------------------------------------------------->')
        raise Exception("Dependencies have unallowed licenses")


if __name__ == "__main__":
    '''
    Search requirements files in whole project
    using pattern requirements*.txt
    '''
    print(os.environ.get("CI_COMMIT_REF_NAME"))
    report = []
    requirement_files = find('requirements*.txt', os.path.dirname(os.path.abspath(__file__)))

    check_files(requirement_files)
    make_report(report)
    

