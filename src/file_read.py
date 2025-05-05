'''
CSCI 410 Final Project
By Cale Voglewede and Nancy Mahlen

file_read.py:
Reads files in test_files directory. Used to read file binaries.

'''

import time
import os

TEST_FILES_PATH = '../test_files'

def get_test_files_list():
    try:
        files = [f for f in os.listdir(TEST_FILES_PATH) if os.path.isfile(os.path.join(TEST_FILES_PATH, f))]
        if files:
            return files
        else:
            print(f"No files found in '{directory_path}'.")
            time.sleep(1)
            return None
    except FileNotFoundError:
        print(f"Error: Directory not found at '{directory_path}'.")
        time.sleep(1)
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(1)
        return None
