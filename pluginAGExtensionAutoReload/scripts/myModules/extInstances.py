from __future__ import print_function
import requests
import json


def getAllInstances(**kwargs):
    extId = kwargs['extId']
    resourcePath = "/api/config/v1/extensions/" + extId + "/instances"
    API_ENDPOINT = kwargs['baseURL'] + resourcePath
    REQHEAD = {'accept': "application/json; charset=utf-8",
               'Authorization': "Api-Token %s" % kwargs['authToken']}

    DATA = requests.get(url=API_ENDPOINT, headers=REQHEAD)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT


def getInstance(**kwargs):
    extId = kwargs['extId']
    configId = kwargs['configId']
    resourcePath = "/api/config/v1/extensions/" + extId + "/instances/" + configId
    API_ENDPOINT = kwargs['baseURL'] + resourcePath
    REQHEAD = {'accept': "application/json; charset=utf-8",
               'Authorization': "Api-Token %s" % kwargs['authToken']}

    DATA = requests.get(url=API_ENDPOINT, headers=REQHEAD)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT


def putInstance(**kwargs):
    extId = kwargs['extId']
    configId = kwargs['configId']
    resourcePath = "/api/config/v1/extensions/" + extId + "/instances/" + configId
    API_ENDPOINT = kwargs['baseURL'] + resourcePath
    REQHEAD = {'Content-Type': "application/json",
               'Authorization': "Api-Token %s" % kwargs['authToken']}
    BODY = kwargs['body']

    DATA = requests.put(API_ENDPOINT, headers=REQHEAD, data=json.dumps(BODY))
    # DATA_DICT = json.loads(DATA.text)
    return DATA  # DATA_DICT
