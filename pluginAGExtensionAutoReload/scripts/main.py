from __future__ import print_function
import requests
import json
from myModules import *


def main():

    # Global Configuration
    baseURL = "https://10.111.32.145/e/environment_id"

    # Get a list of all extensions in production
    allExtensions = getAllExtensions(baseURL=baseURL)

    # Loop through the list and get the statuses of each extension
    # if status is not ok
    # get a list of all the instances of the extension
    # loop through the list of instances and identify the faulty instance
    # restart the faulty instances for N time with certain interval or increasing interval time or one time (preferable)


if __name__ == "__main__":
    main()
