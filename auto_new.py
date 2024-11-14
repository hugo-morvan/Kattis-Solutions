#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script automatically chooses a new problem for you to solve.
The suggestion is made using the suggest function from autokattis.
It then creates a folder in your source directory, and a script inside that folder of your chosen progranning language.
Finally, it prints the link to the problem description both in the file and in the terminal,
as well as the command to submit your code from the terminal using the KattisCLI library.
By default, the problem chosen is of trivial difficulty, but this can be changed with the DIFFICULTY variable.
By default, the programming language for the file creates is python, but this can be changed with the PROG variable

"""

DIFFICULTY = 0 # 0-1 trivial, 2-3 easy, 4-5 moderate, 6-7 hard
PROG = '.py' # change to desired programming language file extension
INCLUDE_PB_LINK_IN_FILE = True
INCLUDE_PB_LINK_IN_CONSOLE = False
INCLUDE_SUBMIT_COMMAND = True
SOURCE_LOCATION = "./source/" #change to desired source directory
import os
from dotenv import load_dotenv
from autokattis import OpenKattis

#Fetch auth from .env
load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASSWORD")
#Initialize connection to Kattis account
kt = OpenKattis(user, password)
                    
def main():

    sug = kt.suggest()

    print(f"\nSelecting problem {sug[DIFFICULTY]['name']} \n")

    if INCLUDE_PB_LINK_IN_CONSOLE:
        print("link: ",sug[DIFFICULTY]["link"],"\n")
    
    path = SOURCE_LOCATION + sug[DIFFICULTY]['name']
    file_name = sug[DIFFICULTY]['pid'] + PROG
    file_path = os.path.join(path, file_name) 

    clean_path = SOURCE_LOCATION + "'" + sug[DIFFICULTY]['name'] + "'"
    clean_file_path = os.path.join(clean_path, file_name) 

    if INCLUDE_SUBMIT_COMMAND:
        submit_command = "kattis " + clean_file_path + " -f\n"
        print("Submit problem using:\n")
        print(submit_command)

    if os.path.exists(path):
        print("A directory already exists for this problem !\n")
    else:
        os.makedirs(path)
        print("The new directory is created!\n")
        with open(file_path, 'w') as f: 
            f.write(f'#{sug[0]["link"]}')

    return 0

if __name__ == "__main__":
    main()