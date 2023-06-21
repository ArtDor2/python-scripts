import os
import re

# specify the directory path
directory_path = input('/path: ')

# loop through all files in the directory
for filename in os.listdir(directory_path):
    # check if the file starts with "["
    if filename.startswith('['):
        # use regex to remove the brackets and text inside them
        new_filename = re.sub(r'\[[^]]*\]\s*', '', filename)
        # use os.rename to rename the file
        os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
        # print(directory_path, new_filename)
