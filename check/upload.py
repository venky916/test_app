import requests
import json
import os

url3='https://api17.ilovepdf.com/v1/upload'

token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuaWxvdmVwZGYuY29tIiwiYXVkIjoiIiwiaWF0IjoxNjk3ODc2NzMxLCJuYmYiOjE2OTc4NzY3MzEsImV4cCI6MTY5Nzg4MDMzMSwianRpIjoicHJvamVjdF9wdWJsaWNfODJhZTI1NTZlMWVkYmY5MDBkMDI2NzJkZTdjZTg0ZGJfSE4wZU9hYjM4NzhiM2ZiZTllNmUzMTc0NjNkYzY0N2I2MzI1NCJ9.KSXiNjV9DXf3Bs_c3VhT5gC9_NQIGwnmnpHoBpl4oMo"
headers = {"Authorization": "Bearer {}".format(token)
}

task={
        "task":"g27d4mrsg3ztmnzAgm5d3njAgfmbgghd71AmgwAct8v9ysdfz7rfl18y4m3n16wtxzpz9gj54z2pvb1tn70vgmAmscty08506q39rdl2ctbd1w8l53tmxh1x58ld2bnptgf9dc4vyc3gchs7yzhdm6rtxy"
}
file={"file":open("Passport_Pic.jpg","rb")}
response=requests.post(url3,headers=headers,data=task,files=file)


print(response.content)
print(response.status_code)

