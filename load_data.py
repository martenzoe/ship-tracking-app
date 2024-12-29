import json

def load_data():
    with open("ships_data.json", "r") as filehandle:
        return json.load(filehandle)

