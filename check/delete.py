import requests

url="https://{server}/v1/upload/{task}/{server_filename}"

response=requests.delete(url)

print(response)