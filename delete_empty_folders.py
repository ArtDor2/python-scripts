import os
import shutil

def is_empty_dir(directory):
    for dirpath, dirnames, files in os.walk(directory):
        if files:
            return False
    return True

def delete(directory):
    empty_dirs = []

    # Loop through all items in the specified directory
    for name in os.listdir(directory):
        path = os.path.join(directory, name)

        # If it's a directory
        if os.path.isdir(path):
            # Check if the directory is empty
            if is_empty_dir(path):
                empty_dirs.append(path)

    if not empty_dirs:
        print("No empty directories found.")
        return

    print("Empty directories:")
    for dir_path in empty_dirs:
        print(dir_path)

    confirm = input("\nDo you want to delete all these directories? (y/n) ")
    if confirm.lower() == 'y':
        # Delete all the empty directories
        for dir_path in empty_dirs:
            shutil.rmtree(dir_path)
            print("Removed directory:", dir_path)
    else:
        print("Operation cancelled, no directories were removed.")

# Run this part only when the script is run directly, not when imported
if __name__ == "__main__":
    # Set the directory where the empty folders will be deleted
    directory = input("Directory: ")  # "C:\\my\\directory\\"
    delete(directory)
