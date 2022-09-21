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
    # print(json.dumps(allExtensions, indent=4))
    as400extension = extensions.getExtension(
        baseURL=baseURL, extId="custom.remote.python.as400_activegate_plugin", authToken=authToken)
    # print(json.dumps(as400extension, indent=4))
    as400extensionStates = extensions.getExtStates(
        baseURL=baseURL, extId="custom.remote.python.as400_activegate_plugin", authToken=authToken)
    print(json.dumps(as400extensionStates, indent=4))
    as400extAllInstances = extInstances.getAllInstances(
        baseURL=baseURL, extId="custom.remote.python.as400_activegate_plugin", authToken=authToken)
    print(json.dumps(as400extAllInstances, indent=4))
    as400extInstance = extInstances.getInstance(
        baseURL=baseURL, extId="custom.remote.python.as400_activegate_plugin", configId="8045620730537405171", authToken=authToken)
    print(json.dumps(as400extInstance, indent=4))
    print('testistsetsetsefsadfa')
    newCfgas400 = as400extInstance
    newCfgas400['enabled'] = False
    newCfgas400['useGlobal'] = False
    newCfgas400['properties']['db_password'] = "P@ssw0rd"
    rm_kw = newCfgas400['properties'].pop('db_password', None) # remove the password fields
    print(json.dumps(newCfgas400))
    as400extinstUpdated = extInstances.putInstance(
        baseURL=baseURL, extId="custom.remote.python.as400_activegate_plugin", configId="8045620730537405171", authToken=authToken, body=newCfgas400)
    print(as400extinstUpdated)

    # Loop through the list and get the statuses of each extension
    # for extension in allExtensions['extensions']:
    #     print(extension['id'])
    #     extStats = extensions.getExtStates(
    #         baseURL=baseURL, extId=extension['id'], authToken=authToken)
    #     print(extStats)
    # if status is not ok
    # get a list of all the instances of the extension
    # loop through the list of instances and identify the faulty instance
    # restart the faulty instances for N time with certain interval or increasing interval time or one time (preferable)


if __name__ == "__main__":
    main()
