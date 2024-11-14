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

def color(s, c):
    return f'\x1b[{c}m{s}\x1b[0m'

def get_rating_color(rating):
    rating = float(rating)
    if rating <= 2.7: return 42
    elif rating <= 5.5 : return 43
    else: return 41

def sug_data(kattis_suggest):
    sug = kattis_suggest
    print("\nHere is a selection of suggested problems:\n")
    ids = range(len(sug))
    data = []
    data.append([color("ID ",1), color("Name",1), color("Difficulty",1), color("Rating",1)])
    for i in ids:
        diff = sug[i]['difficulty']
        diff_color_dict = {'Trivial':34, 'Easy':32, 'Medium':33, 'Hard':31}
        diff_color = diff_color_dict[diff]
        minr = sug[i]['min']
        maxr = sug[i]['max']
        data.append([f"[{color(str(i+1),0)}]",
                     f"{color(sug[i]['name'],0)}",
                     f"{color(diff, diff_color)}",
                     f"[{color(minr, get_rating_color(minr))} - {color(maxr, get_rating_color(maxr))}]"])
    return data, ids

def print_statistics():
    return None

def print_kattis():
    kat = '''                                                                                                                                                            
                                                                              
                                                                              
                                                                              
        @@@@@@@@@@                        @@@@@@@@@                           
       @*:==----:*%@@@                @@@#=:=-=-===@                          
      @@**##=:=======+@@           @@%=======-=+%#+=@                         
      @#*****#%=========%@@@@@@@@@@*========+%******%@                        
      @*********%===@@*::@*:*%:*%:::+@@+===%********#@                        
      @**********@***+==*-%==#=%========*@%**********@                        
      @********@=%========-=========##*#===%#********@                        
      @******@+=#=================%=========+@*******@                        
      @#****@+==================*#===========+@*****%@                        
      @@***@*===#+=*+--+*==========*=:-*++#==+*@****@                         
       @%*#%*==++%=   #+ +=======*: #%:  **#==*+%**@@                         
        @%%*==---# . %.+@ *======+ *:=@- :*=*@@@@*@@                          
         @@@%*:==# . @@@* *======+ =@@%  :*====+%@      @@@@@@@@@@@           
          @*+=====#      *.....:-:=     :%*=-=**@   @@@%*=%#==%==*=*%@        
          @#===:+*=+***+:.:.-:::::.:==:..:=+*@@@@ @@#*%*#+#%=+#+=##++@@       
           @@@-=..:.:.::.:..=@+%-.:..:..:.:.+=+@@@@@%*#***#*++++=*%++@@       
         @@@@+*..:..:..:.:.:.....=%%:.:..:.-==@rrrr@%*******+=+++*%+=@@       
       @@@rr%@*=-..:.:..:.:.:.::%.:.:.::.:===@rrrr@@********=#++++%++@@       
      @@rrrrrr%@===-:...:.:.:....:....:-===@@@@rr%%@#%*#****=%=++=%=*@@@      
      @rrrrr%@rr@%======--:::::::-=====%@@%%%%%%%%%%**%@***=%+++=#+*%*@@     
      @rrrrrrrrrrrr@@@#=============*@@%%%%%%%%%%%%%%**%@***+#++++*=*##@@@@   
      @@rrrrrr%@%@%%%%%%%%@@@%%%%*#@%%%%%%%%%%%%%%%%@**%@****#*+++++#+@%%%@@  
       @rrrrrr%@%%%%%%%%%%%%%%@%#@%%%%%%%%%%%%%%%%%%@**%%****++++++=%@%%%%%@@ 
      @@@@%%%%%%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@#*%***#*=%=+++=%%%%%%%%@@
   @@@%%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%***%+#*+==*+@%%%%%%%@@
 @@@%%%%%%@%@%@==*@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%**%*%**%%++#@%%%%%%%%@@
@@%%%%%%@=.: --...::..+@%%%%%%%%%%%%%%%%%%%%%%%%%%%@%#####***********##%@%%%@@
@@@@@@@@@%%%@%%%@@%%@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
    kattis = '''
         _  __     _   _   _     
        | |/ /__ _| |_| |_(_)___ 
        | ' // _` | __| __| / __|
        | . \ (_| | |_| |_| \__ \ 
        |_|\_\__,_|\__|\__|_|___/
          
          '''
    kat = kat.replace('@', color('@', 30))\
             .replace('.',color('.',1))\
             .replace(':',color(':',1))\
             .replace('%',color('%',30))\
             .replace('=',color('=',33))\
             .replace('*',color('*',33))\
             .replace('+',color('+',33))\
             .replace('-',color('-',33))\
             .replace('#',color('#',30))\
             .replace('r',color('%',31))
    print(kat)
    print(kattis)
    return None
def main():
    """ Main program """
    print_kattis()
    reply = None
    while 1:
        reply = input("\nWhat do you want ? see (s)olved problems statistics or start a (n)ew problem: ")
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
            selection = int(input("Select a problem [id#] or quit (0): "))
            if selection==0:
                print("\nQuitting the program\n")
                return 0
            if selection not in ids:
                print("Please select a valid problem [id#] or quit (0): ")
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