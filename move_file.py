"""
This srcipt moves all files in a folder to a new folder with the same name as the file extension.
This script helps you use the build.py script if you had not all your kattis submission in seperated folders.
"""

import os
import shutil

# Define the source folder path
source_folder = "your_folder_conating_files"

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    # Get the file name
    name = os.path.splitext(filename)[0]

    # Create a new folder with the same name as the file extension
    new_folder = os.path.join(source_folder, name)
    os.makedirs(new_folder, exist_ok=True)

    # Move the file to the new folder
    old_path = os.path.join(source_folder, filename)
    new_path = os.path.join(new_folder, filename)
    shutil.move(old_path, new_path)
