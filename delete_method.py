import requests
import json

url ="https://api.trello.com/1/boards/63ad5affd766424c9a80e1ed"

query = {
    "key" : "17263acf5e8fb7b7c21635588aec6672",
    "token" : "ATTA582b14a0c914afbc54c6e9c105dbdb142890107e9ba2caadbdc60aa4312ef864E6D728CC"}


response = requests.delete(url,params=query)

# cetak response code
print(response.status_code)

# cetak json file
json_response = json.loads(response.text)

print(json_response)