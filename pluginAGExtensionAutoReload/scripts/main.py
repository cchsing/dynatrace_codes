from __future__ import print_function
import requests
import json
from myModules import extensions, extInstances, config


def main():

    # Global Configuration
    # baseURL = "https://10.111.32.145/e/environment_id" # CIMB URL
    baseURL = "https://isl56514.live.dynatrace.com"
    authToken = config.tokens[0]['Token']

    # Get a list of all extensions in production
    allExtensions = extensions.getAllExtensions(
        baseURL=baseURL, authToken=authToken)
    # Loop through the list and get the statuses of each extension
    for extension in allExtensions['extensions']:
        extStats = extensions.getExtStates(
            baseURL=baseURL, extId=extension['id'], authToken=authToken)
        for endpoint in extStats['states']: 
            if endpoint['state'] != 'OK' and endpoint['endpointId']:
                print(extStats)
                endpointCfg = extInstances.getInstance(
                    baseURL=baseURL, extId=endpoint['extensionId'], configId=endpoint['endpointId'], authToken=authToken)
                remove_properties = endpointCfg.pop('properties', None)
                endpointCfg['enabled'] = True
                endpointCfg['useGlobal'] = False
                updateEndpointCfg = extInstances.putInstance(
                    baseURL=baseURL, extId=endpoint['extensionId'], configId=endpoint['endpointId'], authToken=authToken, body=endpointCfg)
                print(updateEndpointCfg)


if __name__ == "__main__":
    main()
