import requests
import json

API_ENTRY_POINT1 = "https://api.ilovepdf.com/v1/"
API_ENTRY_POINT2="https://api.ilovepdf.com/v1/start/"
TASKS = ("merge","compress", "imagepdf", "unlock","extract")

class ILovePdf:
    def __init__(self, public_key):
        """
        You must register in order to get the keys.
        public_key: It can be obtained from
                    https://developer.ilovepdf.com/user/projects
                    You can see it as "project key" or "jti claim"
        secret_key: It can be obtained from
                    https://developer.ilovepdf.com/user/projects
        """
        self.public_key = public_key
        check={
            "public_key":self.public_key
        }
        url="{}".format(API_ENTRY_POINT1)
        response = requests.post(url,json=check).json()
        print(response['token'])
        self.token=response['token']
        self.headers = {"Authorization": "Bearer {}".format(self.token)}

    def new_task(self, task):
        self.files = []
        self.task = task
        url = "{}/{}".format(API_ENTRY_POINT2, task)
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

    def download(self, output_filename=None):
        url = self.base_api_url + "/download/{}".format(self.task_id)
        response = requests.get(url, headers=self.headers)
        output_filename = self.__get_output_filename(
            output_filename
        )
        with open(output_filename, "wb") as output_file:
            output_file.write(response.content)
        return response.status_code

    def __get_output_filename(self, output_filename=None):
        if self.task == "merge":
            filetype = "pdf"
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
        return output_filename


PUBLIC_KEY="project_public_82ae2556e1edbf900d02672de7ce84db_HN0eOab3878b3fbe9e6e317463dc647b63254"  
def test_compress():
    i = ILovePdf(PUBLIC_KEY)
    i.new_task("compress")
    i.add_file("sample.pdf")
    i.execute()
    i.download("out.pdf")
    
test_compress()