from __future__ import print_function
import requests
import json


def getAllInstances(**kwargs):
    extId = kwargs['extId']
    resourcePath = "/api/config/v1/extensions/" + extId + "/instances"
    API_ENDPOINT = kwargs['baseURL'] + resourcePath

    DATA = requests.get(url=API_ENDPOINT)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT


def getInstance(**kwargs):
    extId = kwargs['extId']
    configId = kwargs['configId']
    resourcePath = "/api/config/v1/extensions/" + extId + "/instances/" + configId
    API_ENDPOINT = kwargs['baseURL'] + resourcePath

    DATA = requests.get(url=API_ENDPOINT)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT
