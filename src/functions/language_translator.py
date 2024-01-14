from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

while True:
    text = input("> ")
    print(translate_text(text))