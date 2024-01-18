import requests

url5="https://api8.ilovepdf.com/v1/download/g27d4mrsg3ztmnzAgm5d3njAghxl86ljllkr9j54nxcnjx7hpv983fdgy97xv37ngdl8hh1cqn2lA3gv2k4r2bv0dmyy48s6w3phfzx4dA24xqy563337w5z1A83d4tt6961rlx28bv3mr7Ac1Agw0jy92"

token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuaWxvdmVwZGYuY29tIiwiYXVkIjoiIiwiaWF0IjoxNjk3ODY4OTc4LCJuYmYiOjE2OTc4Njg5NzgsImV4cCI6MTY5Nzg3MjU3OCwianRpIjoicHJvamVjdF9wdWJsaWNfODJhZTI1NTZlMWVkYmY5MDBkMDI2NzJkZTdjZTg0ZGJfSE4wZU9hYjM4NzhiM2ZiZTllNmUzMTc0NjNkYzY0N2I2MzI1NCJ9.eYTCsdOY-p9bjvSNvMFWlPLij9ddCH3zPrxJdnVpK1E"

headers = {"Authorization": "Bearer {}".format(token)}

response=requests.get(url5,headers=headers)

with open("file1.pdf","wb") as f:
    f.write(response.content)

# print(response.content)
print(response.status_code)