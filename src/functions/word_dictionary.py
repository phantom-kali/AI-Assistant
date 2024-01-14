from PyDictionary import PyDictionary
from src.init import tts_instance


def find_meaning(word):
    dictionary = PyDictionary()
    meaning = dictionary.meaning(word)

    if meaning:
        # print(f"Meaning of '{word}':")
        for part_of_speech, definitions in meaning.items():
            # print(f"{part_of_speech.capitalize()}:")
            tts_instance.speak(f"{part_of_speech.capitalize()}:")
            for i, definition in enumerate(definitions[:2], start=1):
                # print(f"  {i}. {definition}")
                tts_instance.speak(f"{i}. {definition}")
    else:
        # print((f"Meaning of '{word}' not found."))
        tts_instance.speak(f"Meaning of '{word}' not found.")
