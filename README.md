# dynatrace_codes

Just a repo for Dynatrace related codes

### Log - 20220909 - 1715

1. Issue with jsonschema when trying to use oneagent_sim for testing the plugin
   error message
   Validating plugin.json against schema
   Error occured: <urlopen error [Errno 2] No such file or directory: 'name.json'>

2. Found the website for this issue url: https://community.dynatrace.com/t5/Extensions/Unable-to-build-oneagent-extension-demo-plugin-in-windows/td-p/193692
3. downgrade the jsonschema to 4.9.1 "pip install jsonschema==4.9.1
