import jwt
import requests
import sys
from PyPDF2 import PdfFileReader
import os

API_ENTRY_POINT = "https://api.ilovepdf.com/v1/start"
TASKS = ("merge", "split", "compress", "pdfjpg", "imagepdf", "unlock",
         "pagenumber", "watermark", "officepdf", "repair", "rotate", "protect",
         "pdfa", "validatepdfa", "extract")
IMPLEMENTED_TASKS = ("merge", "split", "compress", "pdfjpg", "imagepdf")

public_key="project_public_996f41edca7527bd259495b4245ca709_XquPi3d2b8d4fefc0fde85588ddb1bf5cbea2"
secret_key="secret_key_a84e46af13e35a1a258ebd51dc224a29_TVBIi54d095cdf482bb14f34464a0dc6f8ab3"
class ILovePdf:
    def __init__(self, public_key, secret_key, verbose=False):
        """
        You must register in order to get the keys.
        public_key: It can be obtained from
                    https://developer.ilovepdf.com/user/projects
                    You can see it as "project key" or "jti claim"
        secret_key: It can be obtained from
                    https://developer.ilovepdf.com/user/projects
        """
        self.public_key = public_key
        self.secret_key = secret_key
        signed_public_key = (
            {"jti": self.public_key},
            self.secret_key
        )
        self.headers = {"Authorization": "Bearer {}".format(signed_public_key)}

    def new_task(self, task):
        if task not in TASKS:
            self.logger.error(
                "Chosen task '{}' is not available".format(task)
            )
            sys.exit()
        if task not in IMPLEMENTED_TASKS:
            self.logger.error(
                "Chosen task '{}' is not yet implemented".format(task)
            )
            sys.exit()

        self.files = []
        self.task = task
        url = "{}/{}".format(API_ENTRY_POINT, task)

        response = requests.get(url, headers=self.headers).json()
        self.server = response["server"]
        self.task_id = response["task"]
        self.base_api_url = "https://{}/v1".format(self.server)

    def add_file(self, filename):

        url = self.base_api_url + "/upload"
        params = {"task": self.task_id}
        files = {"file": open(filename, "rb")}

        response = requests.post(
            url,
            params,
            files=files,
            headers=self.headers
        ).json()
        self.server_filename = response["server_filename"]
        self.files.append({
            "server_filename": response["server_filename"],
            "filename": filename
        })

    def execute(self, **kwargs):
        url = self.base_api_url + "/process"
        fixed_params = {
            "task": self.task_id,
            "tool": self.task,
            "files": self.files
        }
        params = fixed_params.copy()
        params.update(kwargs)

        response = requests.post(url, json=params, headers=self.headers).json()
        self.timer = response["timer"]

    def download(self, output_filename=None, overwrite=False):
        url = self.base_api_url + "/download/{}".format(self.task_id)

        response = requests.get(url, headers=self.headers)
        output_filename = self.__get_output_filename(
            output_filename, overwrite
        )
        with open(output_filename, "wb") as output_file:
            output_file.write(response.content)

        return response.status_code

    def __get_output_filename(self, output_filename=None, overwrite=False):
        if self.task == "merge":
            filetype = "pdf"
        elif self.task in ["split", "pdfjpg"]:
            filetype = "zip"
        else:
            if len(self.files) == 1:
                filetype = "pdf"
            else:
                filetype = "zip"
        if output_filename:
            ft = output_filename[-3:]
            if ft != filetype:
                output_filename += ("." + filetype)
        else:
            output_filename = "out." + filetype
        overwritable_tasks = [
            "compress", "unlock", "pagenumber", "watermark", "repair",
            "rotate", "protect", "pdfa", "validatepdfa", "extract"
        ]
        if overwrite and filetype == "pdf" and self.task in overwritable_tasks:
            output_filename = self.files[0]["filename"]
        return output_filename

def test_merge():
    i = ILovePdf(public_key,secret_key)
    i.new_task("merge")
    for _ in range(3):
        i.add_file("new_resume.pdf")
    i.execute()
    i.download("out.pdf")
    input_file = PdfFileReader(open("test.pdf", "rb"))
    output_file = PdfFileReader(open("out.pdf", "rb"))
    assert output_file.getNumPages() == 3 * input_file.getNumPages()
    os.remove("out.pdf")
    
test_merge()