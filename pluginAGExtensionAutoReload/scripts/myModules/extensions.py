from __future__ import print_function
import requests
import json


def getAllExtensions(**kwargs):
    resourcePath = "/api/config/v1/extensions"
    API_ENDPOINT = kwargs['baseURL'] + resourcePath

    DATA = requests.get(url=API_ENDPOINT)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT


def getExtStates(**kwargs):
    extId = kwargs['extId']
    resourcePath = "/api/config/v1/extensions/" + extId + "/states"
    API_ENDPOINT = kwargs['baseURL'] + resourcePath

    DATA = requests.get(url=API_ENDPOINT)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT
