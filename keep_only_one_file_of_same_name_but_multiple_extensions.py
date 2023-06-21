# A Python script that will keep only one file with a given extension, if there are several other files with the same name but different extensions in a specified directory, 
import os

# Set the directory where the files will be processed
directory = input("dir: ") # C:\\my\\directory\\"

# Set the file extension that will be kept (e.g., ".txt")
# file_extension = ".epub" # input("ext to keep: ") # "".txt"
file_extension = input("ext to keep: ") # "".txt"

# Initialize an empty dictionary to store the names of the processed files
processed_files = {}
file_num = 1

# Loop through all files in the specified directory
for filename in os.listdir(directory):
  # Skip files that do not exist or are not files
  if not os.path.isfile(os.path.join(directory, filename)):
    continue
  print("cur: ", file_num, filename)
  file_num += 1
  # Check if the file has the specified file extension
  if filename.endswith(file_extension):
    # Get the base name of the file (without the extension)
    basename = os.path.splitext(filename)[0]

    # Check if the base name of the file has been processed
    if basename not in processed_files:
      # Add the base name of the file to the dictionary of processed files
      processed_files[basename] = True

      # Loop through all files with the same base name
      for other_filename in os.listdir(directory):
        # Skip files that do not exist or are not files
        if not os.path.isfile(os.path.join(directory, other_filename)):
          continue

        # Check if the file has the same base name but a different extension
        if os.path.splitext(other_filename)[0] == basename and other_filename != filename:
          # Delete the file
          os.remove(os.path.join(directory, other_filename))
          print("REM:", directory, other_filename)