import requests
import json
import jsonpath

url= "https://reqres.in/api/users?page=2"
response=requests.get(url)
"""print(request)

print(request.content)
print(request.headers)"""

json_response = json.loads(response.text)
print(json_response)

pages=jsonpath.jsonpath(json_response,'total_pages')
assert pages[0] == 2




