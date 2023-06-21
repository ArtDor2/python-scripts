import os
import re

# specify the directory path
directory_path = input('/path: ')

# loop through all directories and files in the directory and its subdirectories
for root, dirs, files in os.walk(directory_path):
    for filename in files:
        # replace spaces with dots, make lowercase, and remove symbols and dashes
        new_filename = re.sub(r'[^\w\s-]', '', filename.lower()).strip().replace(' ', '.').replace('-', '')
        # use os.rename to rename the file
        os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
