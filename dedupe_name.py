import os
import difflib

#TODO TEST IF WORKING

def find_similar_files(dir_path):
    # Dictionary to hold filename and its full path
    file_dict = {}

    # Walk through the directories and files
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_dict[filename] = os.path.join(dirpath, filename)

    # Compare each file with every other file
    for file1 in file_dict:
        for file2 in file_dict:
            if file1 != file2:
                similarity = difflib.SequenceMatcher(None, file1, file2).ratio()
                # If similarity is more than or equal to 90%
                if similarity >= 0.9:
                    file1_path = file_dict[file1]
                    file2_path = file_dict[file2]
                    # If length of file1 is less than file2
                    if os.path.getsize(file1_path) < os.path.getsize(file2_path):
                        print(f"Files {file1_path} and {file2_path} are similar.")
                        response = input("Do you want to delete the smaller file? (yes/no): ")
                        if response.lower() == 'yes':
                            os.remove(file1_path)
                            print(f"Deleted {file1_path}.")
                            del file_dict[file1]  # Remove from dict to avoid re-checking
                            break  # Move on to the next file

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    find_similar_files(directory_path)
