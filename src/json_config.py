'''
CSCI 410 Final Project
By Cale Voglewede and Nancy Mahlen

json_config.py:
Loads necessary data from supported_files.json

'''
import json
import time

CONFIG_PATH = "../config/supported_files.json"

def print_supported_files():

    config = open_json_file()

    if config is None:
        return None

    supported_files = config.get("supported_files")

    if supported_files is None:
        return None

    print('Supported File Types: ')

    for file in supported_files.keys():
        print(f'\t{file}')
        time.sleep(.5)

    time.sleep(2)

def open_json_file() -> dict:

    try:
        with open(CONFIG_PATH, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{file_path}'. Check the file format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def get_file_types_and_signatures() -> dict:
    
    config = open_json_file()

    if config is None:
        return None

    supported_files = config.get("supported_files")

    if supported_files is None:
        return None

    type_to_signature = {}

    for file in supported_files:
        type_to_signature[file] = supported_files[file]['file_signature']


    return type_to_signature 
