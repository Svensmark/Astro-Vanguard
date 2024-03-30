import json
from pathlib import Path



class File_reader():
    def __init__(self, file_path):
        # Read variables json
        script_location = Path(__file__).absolute().parent
        file_location = script_location / file_path
        f = open(file_location, 'r')
        self.json = json.load(f)

    def read_animation_array(self, *argv):
        json = self.json
        for arg in argv:
            json = json[arg]
        return json
    
    def read_json(self):
        return self.json
        