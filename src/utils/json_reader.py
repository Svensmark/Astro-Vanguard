"""
Module for reading JSON files
"""
import json
from pathlib import Path

class FileReader:
    """
    Class for reading JSON files
    """

    @staticmethod
    def read_json(file_path: str):
        """
        Read a JSON file and return its content
        """
        script_location = Path(__file__).absolute().parent
        file_location = script_location / 'json' / file_path
        with open(file_location, 'r', encoding='utf-8') as file:
            json_loaded = json.load(file)
        return json_loaded
