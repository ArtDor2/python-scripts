import os
import shutil

# Ask the user for the directory
source_dir = input("Please enter the directory: ")

# Get list of all files in directory
file_list = os.listdir(source_dir)

# Extract unique extensions
extensions = set()
for file_name in file_list:
    _, extension = os.path.splitext(file_name)
    if extension:  # non-empty extension
        extensions.add(extension)

# Iterate over unique extensions
for extension in extensions:
    # Create the destination directory
    dest_dir = os.path.join(source_dir, extension.strip('.'))
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over all files in the source directory
    for file_name in file_list:
        # Check if this file has the target extension
        if file_name.endswith(extension):
            # Construct full file path
            source = os.path.join(source_dir, file_name)
            destination = os.path.join(dest_dir, file_name)
            # Move the file
            shutil.move(source, destination)

print(f"All files have been moved to their respective directories.")
