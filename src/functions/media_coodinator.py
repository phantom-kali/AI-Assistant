import sys
sys.path.append('AI-Assistant/src/')

from functions.film_extractor import extract_video_title
from functions.music_extractor import extract_song_and_artist

from functions.VideoPlayer import play_video
from functions.MusicPlayer import play_music

import random
import sys
sys.path.append('AI-Assistant/src/')
from src.init import tts_instance

compliments = [
    "is an exceptional artist!",
    "has an incredible talent!",
    "is truly outstanding in the music industry!",
    "deserves all the praise for their musical skills!",
    "is a musical genius!",
]


def play_video_now(text):
    found_video = extract_video_title(text)
    if found_video != None:
        play_video(found_video)
    else:
        tts_instance.speak("video title not detected")


def play_music_now(text):
    song, artist = extract_song_and_artist(text)
    if artist:
        tts_instance.speak(f"{artist} {random.choice(compliments)}")
        tts_instance.speak(f"checking {artist}'s {song}...")
    play_music(song)

