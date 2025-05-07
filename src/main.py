'''
CSCI410/610 Final Project
By Cale Voglewede and Nancy Mahlen

main.py:
Main runtime function of the project, handles user interaction

'''
import os
import time
from json_config import print_supported_files
from file_read import get_test_files_list, identify_file

def main():

    input_1 = ''
    BASE_PATH = os.path.join(os.path.dirname(__file__), '.')
    os.chdir(BASE_PATH)
    clear()
        
    print('CSCI410/610 Final Project '
          'By Cale Voglewede and Nancy Mahlen\n')

    while(True):

        input_1 = input(
        'Please press a key then enter to execute a '
        'corresponding program module:\n\n'
        '[a] - File Identification Simulation\n'
        '[b] - Individual File Identification\n'
        '[c] - Display Supported Files\n'
        '[q] - Exit the Program\n\n'
        'Key: '
        )
        if (input_1 == 'a'):
            simulate_file_identification()

        if (input_1 == 'b'):
            clear()
            identify_one_file()

        if (input_1 == 'c'):
            clear()
            print_supported_files()

        if (input_1 == 'q'):
            clear()
            return

        clear()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def simulate_file_identification():
    
    file_list = get_test_files_list()

    if file_list is None:
        return

    file_list.remove('file_key.txt') # for identifying files manually
    file_list.sort()

    for file in file_list:
        clear()
        print(f'Identifying file type of {file}...\n')
        time.sleep(2)
        identify_file(file) 
        time.sleep(1)
        press_enter_to_continue()


def identify_one_file():

    number_input = ''
    file_list = get_test_files_list()

    if file_list is None:
        return

    file_list.remove('file_key.txt') # for identifying files manually
    file_list.sort()
    file_choices = map_files_to_numbers(file_list)
    file_choices_reversed = {value: key for key, value in file_choices.items()}

    print('Choose a file to identify:')
    for file in file_choices:
        print(f'\t[{file_choices[file]}] for {file}')

    number_input = input('\nKey: ')

    try:
        number_input = int(number_input) 
    except ValueError:
        return

    if (number_input not in file_choices_reversed):
        return

    clear()
    print(f'Identifying file type of {file_choices_reversed[number_input]}...\n')
    time.sleep(2)
    identify_file(file_choices_reversed[number_input])
    time.sleep(1)
    press_enter_to_continue()

def map_files_to_numbers(file_list:list) -> dict:

    file_choices = {}

    for index, element in enumerate(file_list):
        file_choices[element] = index

    return file_choices

def press_enter_to_continue():
    key = input('Press enter to continue: ')


if __name__ == '__main__':
    main()
