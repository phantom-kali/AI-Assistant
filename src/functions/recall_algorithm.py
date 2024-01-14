import re
from datetime import datetime

def recall_first_chat(user_input):

    def parse_log_entry(entry):
        match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - INFO - (User|Intent|Response): (.+)', entry)
        if match:
            timestamp_str, category, content = match.groups()
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
            return timestamp, category, content
        return None

    def identify_first_and_last_user_input(log_entries):
        user_inputs = [parse_log_entry(entry) for entry in log_entries if 'User' in entry]

        first_user_input = user_inputs[0][2] if user_inputs else None
        last_user_input = user_inputs[-1][2] if user_inputs else None
        
        if first_user_input:
            print(first_user_input)
        else:
            print("I forgot")

    # Read log file into a list of entries
    with open('src/logs/conversation.log', 'r') as file:
        log_entries = file.readlines()

    # Identify first and last user input
    first_user_input, last_user_input = identify_first_and_last_user_input(log_entries)
    return first_user_input, last_user_input

def recall_last_chat(user_input):

    def parse_log_entry(entry):
        match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - INFO - (User|Intent|Response): (.+)', entry)
        if match:
            timestamp_str, category, content = match.groups()
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
            return timestamp, category, content
        return None

    def identify_first_and_last_user_input(log_entries):
        user_inputs = [parse_log_entry(entry) for entry in log_entries if 'User' in entry]

        first_user_input = user_inputs[0][2] if user_inputs else None
        last_user_input = user_inputs[-1][2] if user_inputs else None

        return first_user_input, last_user_input

    # Read log file into a list of entries
    with open('src/logs/conversation.log', 'r') as file:
        log_entries = file.readlines()

    # Identify first and last user input
    first_user_input, last_user_input = identify_first_and_last_user_input(log_entries)
    if last_user_input:
        print(last_user_input)
    else:
        print("look at the screen")
