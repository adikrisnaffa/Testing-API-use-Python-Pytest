from os import read
import requests
import json
import pytest
import jsonpath

def test_put_method():
    url = "https://api.trello.com/1/boards/63ae4e01e5dcee007ed7c339"
    file = open("C:\\Users\\Adikrisna\\Documents\\Belajar Test API\\post.json","r")
    request_json = json.loads(file.read())
    response = requests.put(url,json=request_json)
    Code = response.status_code
    assert Code == 200
    json_response = json.loads(response.text)
    Name = jsonpath.jsonpath(json_response,"name")
    assert Name[0] == "Test Via Pytest 3 Baru"
