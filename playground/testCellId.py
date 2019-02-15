import requests
import json

with open("./cellIdToken.json") as json_file:
    json_data = json.load(json_file)

url = "https://us1.unwiredlabs.com/v2/process.php"

token = json_data['token']

payload = {
    "token": token,
    "radio": "gsm",
    "mcc": 724,
    "mnc": 5,
    "cells": [{
        "lac": 13985,
        "cid": 20275
    }],
    "address": 1
}
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers).json()

print(response)
