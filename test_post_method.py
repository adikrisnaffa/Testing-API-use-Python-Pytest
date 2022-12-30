from os import read
import requests
import json
import pytest
import jsonpath

def test_post_method():
    url = "https://api.trello.com/1/boards/"
    file = open("C:\\Users\\Adikrisna\\Documents\\Belajar Test API\\post.json","r")
    request_json = json.loads(file.read())
    response = requests.post(url,json=request_json)
    Code = response.status_code
    assert Code == 200
    json_response = json.loads(response.text)
    Name = jsonpath.jsonpath(json_response,"name")
    assert Name[0] == "Test Via Pytest 3 Baru"
