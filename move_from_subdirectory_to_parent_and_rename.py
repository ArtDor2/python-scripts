import os
import shutil
# import delete_empty_folders

# Set the parent directory where the files will be moved
parent_dir = input("directory: ")  # "C:\\parent\\directory\\"

# Loop through all subdirectories in the parent directory
for dirpath, dirnames, filenames in os.walk(parent_dir):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)

        # Continue the loop if the current path is not a file
        if not os.path.isfile(file_path):
            continue

        # Get the relative path from the parent directory to the file
        relpath = os.path.relpath(dirpath, parent_dir)

        # Replace directory separators with underscores
        new_filename = os.path.join(relpath, filename).replace(os.sep, '_')
        print("moved: ", new_filename)
        
        # Move and rename the file from the subdirectory to the parent directory
        shutil.move(file_path, os.path.join(parent_dir, new_filename))

# After all files have been moved, delete empty directories
# delete_empty_folders.delete(parent_dir)
