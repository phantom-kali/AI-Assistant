import string

def remove_punctuation(input_str):
    return input_str.translate(str.maketrans("", "", string.punctuation))

def extract_video_title(user_input):
    cleaned_input = remove_punctuation(user_input.strip())

    action_keywords = ['watch', 'play film', 'play video']

    # Check if any of the action keywords are present in the cleaned input
    for action_keyword in action_keywords:
        if action_keyword in cleaned_input.lower():
            # Find the word after the action keyword
            word_start = cleaned_input.lower().find(action_keyword) + len(action_keyword)
            remaining_text = cleaned_input[word_start:].strip()

            if remaining_text:
                return remaining_text.lower()

    return None


