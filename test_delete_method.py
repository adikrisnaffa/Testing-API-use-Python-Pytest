import requests
import json
import jsonpath
import pytest

def test_delete_method():
    url = "https://api.trello.com/1/boards/63ad60f551cf8800520ec516"

    query = {
    "key" : "17263acf5e8fb7b7c21635588aec6672",
    "token" : "ATTA582b14a0c914afbc54c6e9c105dbdb142890107e9ba2caadbdc60aa4312ef864E6D728CC"}

    response = requests.delete(url,params=query)

    Code = response.status_code

    assert Code

    json_response = json.loads(response.text)

    nilai = jsonpath.jsonpath(json_response,"_value")
    
    assert nilai[0] == None