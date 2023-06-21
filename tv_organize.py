import os
import re
import shutil
from collections import defaultdict

# Change this to your desired directory
source_dir = input('/path')

def create_series_folder(series_name):
    series_folder = os.path.join(source_dir, series_name)
    if not os.path.exists(series_folder):
        os.makedirs(series_folder)
    return series_folder

def get_series_and_episode(filename):
    # Regex patterns to match series name and episode number
    patterns = [
        r'^(.+?)\s[Ss]?(\d+)[Ee](\d+).*\.(mkv|avi|mp4|mov)$',
        r'^(.+?)\.s(\d{2})e(\d{2}).*\.(mkv|avi|mp4|mov)$',
        r'^(.+?)\.\(.*\)\.ep\.(\d{2}).*\.(mkv|avi|mp4|mov)$',
        r'^(.+?)\.(\d{2}).*\.(mkv|avi|mp4|mov)$'
    ]

    for pattern in patterns:
        match = re.search(pattern, filename)

        if match:
            series_name = match.group(1).replace('.', ' ').strip()
            season_num = 1  # Assuming season 1 for this format
            episode_num = int(match.group(2))
            return series_name, season_num, episode_num

    return None, None, None

# Count episodes per series
series_counter = defaultdict(int)

for entry in os.scandir(source_dir):
    if entry.is_file():
        filename = entry.name
        series_name, season_num, episode_num = get_series_and_episode(filename)

        if series_name:
            series_counter[series_name] += 1

# Print series folders to be created
print("Series folders to be created:")
for series_name, count in series_counter.items():
    if count >= 5:
        print(f"{series_name} ({count} episodes)")

# Ask for user confirmation
confirmation = input("Proceed with moving episodes? (y/n): ")

if confirmation.lower() == 'y':
    # Move episodes to folders if there are at least 5 episodes per series
    for entry in os.scandir(source_dir):
        if entry.is_file():
            filename = entry.name
            series_name, season_num, episode_num = get_series_and_episode(filename)

            if series_name and series_counter[series_name] >= 5:
                series_folder = create_series_folder(series_name)
                old_path = os.path.join(source_dir, filename)
                new_path = os.path.join(series_folder, filename)
                shutil.move(old_path, new_path)
                print(f'Moved {filename} to {series_folder}')
else:
    print("Operation canceled.")
