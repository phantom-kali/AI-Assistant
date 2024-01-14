import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

import sys
sys.path.append('AI-Assistant/src/')
from src.init import tts_instance


def search_files_folders(root, target_name, allowed_extensions):
    found_items = []
    for entry in os.scandir(root):
        if entry.is_dir():
            found_items.extend(search_files_folders(entry.path, target_name, allowed_extensions))
        elif target_name.lower() in entry.name.lower() and entry.is_file() and entry.name.lower().endswith(allowed_extensions):
            found_items.append(entry.path)
    return found_items


def concurrent_search(start_path, target_name, allowed_extensions):
    start_path = Path(start_path).expanduser()
    found_items = []

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(search_files_folders, start_path, target_name, allowed_extensions)]
        for future in futures:
            found_items.extend(future.result())

    return found_items


def play_videos(start_path, target_name):
    allowed_video_extensions = (".mp4", ".mkv", ".avi")
    video_files = concurrent_search(start_path, target_name, allowed_video_extensions)

    if not video_files:
        print(f"No video files found for: {target_name}")
        tts_instance.speak("Video not found")
        return

    # print(f"Found video files for {target_name}:\n")
    for i, video_file in enumerate(video_files, start=1):
        print(f"{i}. {video_file}")

    while True:
        try:
            choice = int(input("\nEnter the number of the video to play (0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(video_files):
                selected_video = video_files[choice - 1]
                print(f"\nPlaying: {selected_video}")
                os.system(f"gnome-terminal -- vlc '{selected_video}'")
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_video(target_name):
    start_path = "Videos"
    tts_instance.speak(f"searching for {target_name}")
    concurrent_search(start_path, target_name, (".mp4", ".mkv", ".avi"))

    play_videos(start_path, target_name)
