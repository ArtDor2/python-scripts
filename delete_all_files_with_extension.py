# Here is a Python script that will delete all files with a specified file extension in a given directory, and print the names of the deleted files:

import os

# Set the directory where the files will be deleted
directory = input("dir: ") # "C:\\my\\directory\\"

# Set the file extension that will be deleted (e.g., ".txt")
file_extension = input("extension to delete: ") #.txt"

# Loop through all files in the specified directory
for filename in os.listdir(directory):
  # Skip files that do not exist or are not files
  if not os.path.isfile(os.path.join(directory, filename)):
    continue

  # Check if the file has the specified file extension
  if filename.endswith(file_extension):
    # Delete the file
    os.remove(os.path.join(directory, filename))

    # Print the name of the deleted file
    print("Deleted file:", filename)