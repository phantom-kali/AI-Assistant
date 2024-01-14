import pywhatkit as kt

import sys
sys.path.append('AI-Assistant/src/')
from init import tts_instance

def get_search_results(query):
    try:
        # Perform a Google search and get the specified number of results
        results = kt.search(query)
        tts_instance.speak("done")
        
    except:
        print("you're not connected to the internet!")



