import os
import re
import shutil

# Ask user for directory
dir_path = input("Enter directory path: ")

# create regex pattern to match tv show name
pattern = r'(.+?)\.s\d{2}'

# iterate through files in directory
for filename in os.listdir(dir_path):
    # check if file is a video file
    if filename.endswith(('.mp4', '.mkv', '.avi')):
        # use regex pattern to extract tv show name
        match = re.search(pattern, filename)
        if match:
            # create folder for tv show if it doesn't exist
            show_folder = match.group(1)
            if not os.path.exists(show_folder):
                os.mkdir(show_folder)
            # move file into tv show folder
            shutil.move(filename, os.path.join(show_folder, filename))
