import json
import os


SETTINGS_FILE = 'settings.json'


# Load Settings
def Load_Settings():

    if not os.path.exists(SETTINGS_FILE):
        return {
            'Currency': '$',
            'Screen Delay': 1
            }

    try:
        with open(SETTINGS_FILE, 'r') as file:
            Settings = json.load(file)

            return Settings

    except json.JSONDecodeError:
        return {
            'Currency': '$',
            'Screen Delay': 1
            }


# Dump Settings
def Dump_Settings(Settings):

    with open(SETTINGS_FILE, 'w') as file:
        json.dump(Settings, file, indent=4)