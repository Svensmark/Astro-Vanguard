import json
from pathlib import Path

class File_reader():
    def __init__(self):
        # Read variables json
        pass


    def read_animation_array(self, *argv):
        json = self.json
        for arg in argv:
            json = json[arg]
        return json

    def read_json(self, file_path: str):
        script_location = Path(__file__).absolute().parent
        file_location = script_location / 'json' / file_path
        f = open(file_location, 'r')
        json_loaded = json.load(f)
        return json_loaded
