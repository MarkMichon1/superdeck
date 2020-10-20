import json

# Load JSON config secret
config_path = '/home/m/Desktop/superdeck-config.json'
with open(config_path) as config_json:
    config_dict = json.load(config_json)