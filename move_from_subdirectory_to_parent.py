import os
import shutil

# Set the parent directory
parent_dir = input("directory: ") # "/path/to/parent/directory"

# Get a list of all subdirectories in the parent directory
subdirs = [d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))]

# Loop through each subdirectory
for subdir in subdirs:
  # Set the path to the current subdirectory
  subdir_path = os.path.join(parent_dir, subdir)
  
  # Get a list of all files in the current subdirectory
  files = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]
  
  # Loop through each file
  for file in files:
    # Set the path to the current file
    file_path = os.path.join(subdir_path, file)
    
    # Move the file up to the parent directory
    shutil.move(file_path, parent_dir)
