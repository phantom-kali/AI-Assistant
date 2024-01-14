from gtts import gTTS
from playsound import playsound
import os


class TextToSpeech:

    @staticmethod
    def speak(text: str):
        if text is not None:
            if text:
                tts = gTTS(text=text, lang='en', slow=False)
                temp_file = "temp.mp3"
                try:
                    tts.save(temp_file)
                    playsound(temp_file)
                    os.remove(temp_file)
                except:
                    pass
