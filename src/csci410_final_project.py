'''
CSCI 410 Final Project
By Cale Voglewede and Nancy Mahlen

csci410_final_project.py:
Main runtime function of the project, handles user interaction

'''
import os
from json_config import print_supported_files

def main():

    exit_flag_1 = False
    input_1 = ''
    BASE_PATH = os.path.join(os.path.dirname(__file__), '.')
    os.chdir(BASE_PATH)
    clear()
        
    print('CSCI 410 Final Project '
          'By Cale Voglewede and Nancy Mahlen\n')

    while(exit_flag_1 == False):

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
            pass

        if (input_1 == 'b'):
            pass

        if (input_1 == 'c'):
            clear()
            print_supported_files()

        if (input_1 == 'q'):
            clear()
            return

        clear()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
