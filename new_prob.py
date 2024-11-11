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
                    
def table(rows):
    max_widths = []
    for column in zip(*rows):
        max_widths.append(max([len(text) for text in column]))
    template = '  '.join(['{{:<{}}}'.format(width) for width in max_widths])
    return '\n'.join([template.format(*row) for row in rows])

def sug_data(kattis_suggest):
    sug = kattis_suggest
    print("Here is a selection of suggested problems")
    ids = range(len(sug))
    data = []
    data.append(["ID", "Name", "Difficulty", "Rating"])
    for i in ids:
        data.append([f"[{i+1}]",f"{sug[i]['name']}",f"{sug[i]['difficulty']}", f"[{sug[i]['min']} - {sug[i]['max']}]"])
    return data, ids

def print_statistics():
    return None

def main():
    """ Main program """
    reply = None
    while 1:
        reply = input("What do you want ? see (s)olved problems statistics or start a (n)ew problem: ")
        if reply=="q":
            print("Quitting the program")
            return 0
        if reply not in ("s","n"):
            print("Invalid choice, please try again or (q)uit")
        else:
            break
    
    if reply=="s":
        print("Here are some statistics about the problems you solved so far")
        #To Do: Print statistics in a nice format
        print_statistics()
    elif reply=="n":
        sug = kt.suggest()
        data, ids = sug_data(sug)
        print(table(data))
        while 1:
            selection = int(input("Select a problem [id] or 0 to quit: "))
            if selection==0:
                print("Quitting the program")
                return 0
            if selection not in ids:
                print("Please select a valid problem id or quit (0): ")
            else:
                break
        sel_id = selection-1
        sel_data = kt.problem(sug[sel_id]['pid'])  
        print(f"You have selected problem {sug[sel_id]['name']} \n")
        print("Description: \n")
        print(sel_data[0]['text'])
        print("\n")

        #print a link to the problem description page
        source_location = "./source/"
        path = source_location + sug[sel_id]['name']
        cd_path = source_location + "'" + sug[sel_id]['name'] + "'"
        #check if folder name already exist
        isExist = os.path.exists(path)
        #if yes, print path to folder (to help with cd)
        if isExist:
            print("A directory already exists for this problem !")
            print("cd", cd_path)
        #if no, create a folder, create a python file with the name of the problem
        else:
            os.makedirs(path)
            print("The new directory is created!")
            # define the file name and path 
            file_name = sug[sel_id]['pid']+".py"
            file_path = os.path.join(path, file_name) 
 
            #create the file 
            with open(file_path, 'w') as f: 
                f.write(f'#{sug[sel_id]["link"]}') 
            print("cd", cd_path)


    return 0

if __name__ == "__main__":
    main()