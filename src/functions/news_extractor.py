import re


def extract_news_category(user_input):
    # Define your news-related action keywords
    action_keywords = ['read', 'fetch']

    # Check if any of the action keywords are present in the user input
    for action_keyword in action_keywords:
        if action_keyword in user_input.lower():
            # Define a regular expression pattern to match the news category
            category_pattern = re.compile(fr'\b{action_keyword}\s+(?:latest\s+)?(\w+)\s+news\b', re.IGNORECASE)

            # Try to find a match using the pattern
            match = category_pattern.search(user_input)
            if match:
                # The first group in the regex captures the news category
                news_category = match.group(1)
                return news_category.lower()

    return None
