import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

file  =  open("C:\\Users\\saivi\\practice\\new_1",'r')
json_input = file.read()
request_json = json.loads(json_input)

response = requests.put(url,request_json)
#print(response.content)

assert response.status_code == 200

response_json = json.loads(response.text)
updated_list = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_list[0])

