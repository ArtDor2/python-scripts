import os
import shutil

source_dir = input('/path/to/source/directory')

# iterate through all files in the source directory
for file_name in os.listdir(source_dir):
    # check if the file is a regular file (not a directory)
    if os.path.isfile(os.path.join(source_dir, file_name)):
        # create a directory with the same name as the file
        new_dir_path = os.path.join(source_dir, os.path.splitext(file_name)[0])
        os.makedirs(new_dir_path, exist_ok=True)
        
        # move the file to the new directory
        old_file_path = os.path.join(source_dir, file_name)
        new_file_path = os.path.join(new_dir_path, file_name)
        shutil.move(old_file_path, new_file_path)
