import string

def remove_punctuation(input_str):
    return input_str.translate(str.maketrans("", "", string.punctuation))

def extract_song_and_artist(user_input):
    cleaned_input = remove_punctuation(user_input.strip())  # Trim whitespaces

    action_keywords = ['play song', 'play', 'play track']

    # Check if any of the action keywords are present in the cleaned input
    for action_keyword in action_keywords:
        if action_keyword in cleaned_input.lower():
            # Find the word after the action keyword
            word_start = cleaned_input.lower().find(action_keyword) + len(action_keyword)
            remaining_text = cleaned_input[word_start:].strip()

            # Check if ' by ' is present in the remaining text
            if ' by ' in remaining_text:
                song, artist = remaining_text.split(' by ', 1)
                return song.strip().lower(), artist.strip().lower() if artist else None
            else:
                # Check if the remaining text is not empty
                if remaining_text:
                    return remaining_text.lower(), None

    return None


