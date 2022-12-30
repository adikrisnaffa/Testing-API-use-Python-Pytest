from os import read
import requests
import json

url = "https://api.trello.com/1/boards/63ae4e01e5dcee007ed7c339"

file = open("C:\\Users\\Adikrisna\\Documents\\Belajar Test API\\post.json","r")

request_json = json.loads(file.read())

response = requests.put(url,json=request_json)

# cetak response code
print(response.status_code)

#cetak json file
json_response = json.loads(response.text)

print(json_response)