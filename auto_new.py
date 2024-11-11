#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    """ Main program """
    sug = kt.suggest()

    print(f"Selecting problem {sug[0]['name']} \n")
    print("link: ",sug[0]["link"],"\n")
    
    source_location = "./source/"                   #change to desired source directory
    path = source_location + sug[0]['name']
    file_name = sug[0]['pid']+".py"
    file_path = os.path.join(path, file_name) 

    clean_path = source_location + "'" + sug[0]['name'] + "'" #to take care of the spaces in folders names
    clean_file_path = os.path.join(clean_path, file_name) 
    submit_command = "kattis " + clean_file_path + " -f"
    print(submit_command)

    if os.path.exists(path):
        print("A directory already exists for this problem !")

    else:
        os.makedirs(path)
        print("The new directory is created!")
        with open(file_path, 'w') as f: 
            f.write(f'#{sug[0]["link"]}')

    return 0

if __name__ == "__main__":
    main()