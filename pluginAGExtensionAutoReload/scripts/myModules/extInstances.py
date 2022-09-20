from __future__ import print_function
import requests
import json


def main(**kwargs):
    resourcePath = "/api/config/v1/extensions"
    API_ENDPOINT = kwargs['baseURL'] + resourcePath

    DATA = requests.get(url=API_ENDPOINT)
    DATA_DICT = json.loads(DATA.text)
    return DATA_DICT


if __name__ == "__main__":
    main()
