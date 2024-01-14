import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

import sys
sys.path.append('AI-Assistant/src/')
from src.init import tts_instance

def search_files_folders(root, target_name):
    found_items = []
    for entry in os.scandir(root):
        if entry.is_dir():
            found_items.extend(search_files_folders(entry.path, target_name))
        elif target_name.lower() in entry.name.lower() and entry.is_file():
            found_items.append(entry.path)
    return found_items

def concurrent_search(start_path, target_name):
    start_path = Path(start_path).expanduser()
    found_items = []

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(search_files_folders, start_path, target_name)]
        for future in futures:
            found_items.extend(future.result())

    for item in found_items:
        if item.lower().endswith((".mp3", ".m4a")):
            print(item)
            os.system(f"gnome-terminal -- mplayer '{item}'")
            return  # Stop searching after playing the first match

    tts_instance.speak("No such Artist or Music found on this device")

def play_music(target_name):
    start_path = "Music"

    concurrent_search(start_path, target_name)

