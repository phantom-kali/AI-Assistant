import sys

sys.path.append("AI-Assistant/src/functions")

from word_extractor import extract_word
from word_dictionary import find_meaning

from search_extractor import extract_search_keyword
from google_search import get_search_results
from wiki_search import WikipediaSearchGUI
from src.init import tts_instance

def find_word_meaning(phrase):
    word = extract_word(phrase)
    if word:
        find_meaning(word)
    else:
        tts_instance.speak("Unable to extract word, Use specified format!!!")


def google_search(query):
    key_word = extract_search_keyword(query)
    if key_word:
        get_search_results(key_word)
    else:
        tts_instance.speak("Unable to identify search query. Use specified format!!!")


def wiki_search(query):
    key_word = extract_search_keyword(query)
    if key_word:
        WikipediaSearchGUI(key_word)
    else:
        tts_instance.speak("Unable to identify search query. Use specified format!!!")


def terminate(drop_text):
    sys.exit(0)
