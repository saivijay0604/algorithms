import requests
import json
import jsonpath
url = "https://reqres.in/api/users"

file  =  open("C:\\Users\\saivi\\practice\\new_1",'r')
json_input = file.read()
request_json = json.loads(json_input)
response = requests.post(url,request_json)
print(response.content)

assert response.status_code == 201

print(response.headers.get('content-Length'))

response_json = json.loads(response.text)
id=jsonpath.jsonpath(response_json,'id')
print(id[0])