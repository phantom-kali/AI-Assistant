import string

def remove_punctuation(input_str):
    return input_str.translate(str.maketrans("", "", string.punctuation))

def extract_search_keyword(user_input):
    cleaned_input = remove_punctuation(user_input)

    meaning_keywords = ['search on google', 'google', 'wiki', 'search on wikipidia', 'search on wiki']

    # Check if any of the meaning keywords are present in the cleaned input
    for keyword in meaning_keywords:
        if keyword in cleaned_input.lower():
    
            word_start = cleaned_input.lower().find(keyword) + len(keyword)
            word = cleaned_input[word_start:].strip()
            return word.lower()

    return None

