import requests
import json



def getCellData(dict_cellInfo):

    # get token from cellIdToken.json
    with open("cellIdToken.json") as json_file:
        json_data = json.load(json_file)
    
    token = json_data['token']

    # service url
    url = "https://us1.unwiredlabs.com/v2/process.php"

    # mount the payload ande the header
    payload = {
        "token": token,
        "mcc": int(dict_cellInfo['mcc']),
        "mnc": int(dict_cellInfo['mnc']),
        "cells": [{
            "lac": int(dict_cellInfo['lac']),
            "cid": int(dict_cellInfo['cellid'])
        }],
        "address": 1
    }
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }

    # execute POST request getting the response
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers).json()

    return response


