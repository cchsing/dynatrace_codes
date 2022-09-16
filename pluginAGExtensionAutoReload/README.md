# Python Script for Automatic Reloading of the ActiveGate Extensions 

The objective of this program is to automate the process of restarting the Dynatrace ActiveGate Extension whenever the query destination IT asset (Database, etc API) cannot be connected and causing the disabling of schedule query of the ActiveGate Extension. 

## Dependencies
1. Dynatrace API will be used for querying of the extensions' statuses and the restart of the extensions. Thus, python requests module will be used for the standard REST API calls. 
2. PyInstaller will be used for packaging of the program along with its the dependencies and python interpreter. 

## Authentication
1. The Dynatrace authentication method will need to be explored for the API calls. 

## Inputs 
1. Querying of the statuses of all the extensions and decision for restart based on status. 

## Outputs 
1. Handling of the logs for successful restart of the extension.
2. Handling of the logs for unsuccessful restart of the extension. 
