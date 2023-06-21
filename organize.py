import os
import re # string splitting
import json # for sorting dictionary


modifier = -1

def check_if_directory_exists(path):
  return os.path.isdir(path)


def create_folder_for_cat(ext=False):
  if not ext:
    dir_name = 'Un-Classified'
  else:
    ext = ext#.lower()
    dir_name = ext #+ '-Files'
  if not check_if_directory_exists(dir_name):
    os.mkdir(dir_name)
  return dir_name


def list_directory_contents():
  return os.listdir()

def front_or_back():
  if input("front or back") == "front":
    modifier = 0
  else:
    modifier = -1

def get_file_cat(file):
  file_string = file.replace(". ", " ")
  file_string = file_string.replace("- ", " ")
  file_name = re.split('_|\.', file_string)
  remove = ("1080p", "720p", "480p", "1440p", "2160p", "hls", "mp4", "mkv", "webm", "m4a", "part 1", "part 2", "part 3", "", "com", "AAC)")

  for i in remove:
      while i in file_name:
          file_name.remove(i)
          
  if len(file_name) > 1:
      return file_name[modifier]
      print(file_name[modifier])

  return False


def move_file_to_directory(file, dir_name):
  if check_if_directory_exists(dir_name):
    dest_file_name = dir_name + '/' + file
    print('Moving', file, 'to', dest_file_name)
    os.rename(file, dest_file_name)


def main():
  path = input('Enter the absolute path directory to organize:')
  if not check_if_directory_exists(path):
    print('Invalid Path')
    exit()
  os.chdir(path)
  files_and_folders = list_directory_contents()
  front_or_back()

  cat_file_num = {} # make a dictionary of number of files in each category

  # count items in cat
  for item in files_and_folders:
    if item[0] == '.':
      print('Skipping', item)
    elif not check_if_directory_exists(item):
      cat = get_file_cat(item)
      if cat in cat_file_num:
        cat_file_num[cat] = cat_file_num.get(cat) + 1
      else:
          cat_file_num[cat] = 1

  cat_file_num_filtered = {}

  min_cat_num = int(input("enter min categories number: "))

  for item in files_and_folders:
    if item[0] == '.':
      print('Skipping', item)
    elif not check_if_directory_exists(item):
      cat = get_file_cat(item)
      if cat_file_num[cat] > min_cat_num or check_if_directory_exists(cat):
        dir_name = create_folder_for_cat(cat)
        move_file_to_directory(item, dir_name)

        print("[MOVED: CAT:] ", cat, " [ITEM:] ", item, " [DIR:] ", dir_name)
  
  print("##############")
  for cat_id in cat_file_num:
    if cat_file_num[cat_id] > min_cat_num:
        print(cat_id, cat_file_num.get(cat_id))


main()
