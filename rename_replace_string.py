import os

def replace_in_file_names(directory, old_string, new_string):
    # Loop through all files in the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            # Skip directories
            if os.path.isdir(filepath):
                continue

            # Replace the target string in the filename
            new_filename = filename.replace(old_string, new_string)

            # Rename the file
            if new_filename != filename:
                os.rename(filepath, os.path.join(dirpath, new_filename))

# Run this part only when the script is run directly, not when imported
if __name__ == "__main__":
    # Set the directory where the changes will be made
    directory = input("Enter directory path: ")  # e.g., "C:\\my\\directory\\"
    
    # Set the old string and the new string
    old_string = input("Enter string to replace in file names: ")  # e.g., "old"
    new_string = input("Enter replacement string for file names: ")  # e.g., "new"
    
    # Perform the replacement
    replace_in_file_names(directory, old_string, new_string)
