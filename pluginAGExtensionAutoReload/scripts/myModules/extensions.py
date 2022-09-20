from __future__ import print_function
from configparser import ExtendedInterpolation
import requests
import json


def getAllExtensions(**kwargs):
    resourcePath = "/api/config/v1/extensions"
    API_ENDPOINT = kwargs['baseURL'] + resourcePath
    REQHEAD = {'accept': "application/json; charset=utf-8",
               'Authorization': "Api-Token %s" % kwargs['authToken']}

    DATA = requests.get(url=API_ENDPOINT, headers=REQHEAD)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT


def getExtension(**kwargs):
    extId = kwargs['extId']
    resourcePath = "/api/config/v1/extensions/" + extId
    API_ENDPOINT = kwargs['baseURL'] + resourcePath
    REQHEAD = {'accept': "application/json; charset=utf-8",
               'Authorization': "Api-Token %s" % kwargs['authToken']}

    DATA = requests.get(url=API_ENDPOINT, headers=REQHEAD)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT


def getExtStates(**kwargs):
    extId = kwargs['extId']
    resourcePath = "/api/config/v1/extensions/" + extId + "/states"
    API_ENDPOINT = kwargs['baseURL'] + resourcePath
    REQHEAD = {'accept': "application/json; charset=utf-8",
               'Authorization': "Api-Token %s" % kwargs['authToken']}

    DATA = requests.get(url=API_ENDPOINT, headers=REQHEAD)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT
