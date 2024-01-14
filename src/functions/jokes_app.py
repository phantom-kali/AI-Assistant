import pyjokes
from src.init import tts_instance


def get_joke(ignore_text):
    joke = pyjokes.get_joke()
    tts_instance.speak(f"Here's a joke for you: {joke}")

