'''
CSCI 410 Final Project
By Cale Voglewede and Nancy Mahlen

file_read.py:
Reads files in test_files directory. Used to read file binaries.

'''

import time
import os
from json_config import get_file_types_and_signatures

TEST_FILES_PATH = '../test_files/'

def get_test_files_list() -> list:

    try:
        files = [f for f in os.listdir(TEST_FILES_PATH) \
        if os.path.isfile(os.path.join(TEST_FILES_PATH, f))]

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

def identify_file(file_name:str):

    file_path = os.path.join(TEST_FILES_PATH, file_name)
    types_to_signature = get_file_types_and_signatures()

    # shd - smallest hamming distance
    shd_ratio = 1    # ratio needed for comparision across different signature lengths
    shd = 2**16
    shd_difference_file_type = None
    shd_difference_file_signature = None
    shd_difference_original_signature = None
    
    for file_type in types_to_signature:
        file_signature = types_to_signature[file_type]
        num_bytes_to_read = (len(file_signature)//2)    # division by 2 is done since hexadecimal is half a byte
        read_bytes = read_binary_data(file_path, file_type, num_bytes_to_read)
        
        if read_bytes == file_signature:
            print(f'The file type is {file_type} and it has a file signature '
                  f'of 0x{read_bytes}.\n')
            return
        
        hamming_distance = \
        calculate_hamming_distance(read_bytes, file_signature)

        maximum_possible_hd = (len(file_signature)*4) # *4 for hex -> binary
        hamming_distance_ratio = hamming_distance / maximum_possible_hd
        

        if hamming_distance_ratio < shd_ratio:
            shd = hamming_distance
            shd_ratio = hamming_distance_ratio
            shd_difference_file_type = file_type
            shd_difference_file_signature = file_signature
            shd_difference_original_signature = read_bytes

    print(f'Most similar file type found was {shd_difference_file_type}, '
          f'with a hamming distance of {shd}.\n'
          f'\tOriginal file signature: '
          f'\t0x{shd_difference_original_signature}\n'
          f'\tExpected file signature: '
          f'\t0x{shd_difference_file_signature}\n')
            
def calculate_hamming_distance(read_bytes: str, file_signature: str):

    read_bytes_hex = int(read_bytes,16)
    file_signature_hex = int(file_signature,16)
    difference = bin((read_bytes_hex ^ file_signature_hex))[2:]
    hamming_distance = difference.count('1')
    return hamming_distance


def read_binary_data(file_path: str, file_type: str, num_bytes_to_read: int) -> str:

        with open(file_path,'rb') as file:
            read_bytes = file.read(num_bytes_to_read)
            if not read_bytes:
                print('File Read Error')
                return 'N/A'

        read_bytes = read_bytes.hex()
        return read_bytes



