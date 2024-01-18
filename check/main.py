import os
import requests
import json
import jwt

public_key="project_public_82ae2556e1edbf900d02672de7ce84db_HN0eOab3878b3fbe9e6e317463dc647b63254"
secret_key="secret_key_a84e46af13e35a1a258ebd51dc224a29_TVBIi54d095cdf482bb14f34464a0dc6f8ab3"

api_url = "https://api.ilovepdf.com/v1/auth"
api="https://api.ilovepdf.com/v1/start"

headers = {"Authorization": "Bearer {}".format(public_key,secret_key)}

response=requests.post(api_url, headers=headers)

print(response.content)
# def merge_pdfs():
#     # Implement PDF merging logic using ILOVEPDF API
#     #task
#     files = []
#     task = "merge"
#     url = "{}/{}".format(api, task)
#     response = requests.get(url, headers=headers).json()
#     server = response["server"]
#     task_id = response["task"]
#     base_api_url = "https://{}/v1".format(server)
    
#     #add_files
#     filename="new_resume.pdf"
#     url = base_api_url + "/upload"
#     params = {"task": task_id}
#     files = {"file": open(filename, "rb")}

#     response = requests.post(
#         url,
#         params,
#         files=files,
#         headers=headers
#     ).json()
#     server_filename = response["server_filename"]
#     files.append({
#         "server_filename": response["server_filename"],
#         "filename": filename
#     })

#     #execute
#     url = base_api_url + "/process"
#     fixed_params = {
#         "task": task_id,
#         "tool": task,
#         "files": files
#     }
#     params = fixed_params.copy()
#     response = requests.post(url, json=params, headers=headers).json()
#     timer = response["timer"]
    
#     #download
#     url = base_api_url + "/download/{}".format(task_id)
#     response = requests.get(url, headers=headers)
#     output_filename = "out." + "pdf"
#     with open(output_filename, "wb") as output_file:
#         output_file.write(response.content)

#     return response.status_code

# merge_pdfs()