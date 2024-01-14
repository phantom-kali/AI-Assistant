
```markdown
# Chatbot Project

## Setup Instructions

1. **Star and Download:** Star and download this repository.

2. **Virtual Environment:** Create a virtual environment in the cloned/downloaded folder:
   ```bash
   python -m venv .
   ```

3. **Install Dependencies:** Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Replace Assistant Module:** Replace the contents of `lib/python3.x/neuralintents/assistants.py` with the contents of `src/assistants.py`.

5. **Run the Chatbot:** Move to the `src` folder and run:
   ```bash
   python sky_GUI.py
   ```

## Warning

- This chatbot is primarily built on Linux, and some commands are Linux-based. Customize these commands for your operating system.

- If you encounter 'File Not Found' errors, adjust the file paths accordingly.

## Usage

Here are some commands you can use:

## Word Meaning:

    what is the meaning of [word]
    find the meaning of [word]

## Google Search:

    google [query]
    search on google [query]

## Wikipedia Search:

    wiki [query]
    search on wiki [query]
    search on wikipedia [query]

## Play Music:

    play [music_title]
    play [artist_name]

## Play Video:

    watch [video_title]
    play film [video_title]
    play video [video_title]

## Play a Game:

    play game
    play a game

## Read News:

    fetch latest [category] news
    read [category] news
    read some [category] news

## Customization

### Fine-tuning the Chatbot

- Modify chatbot responses: Go to `src/data/intents.json`.

- Introduce new intents: Follow the existing format in `intents.json`.

- Open sky_GUI.py; Comment out assistant.load() and uncomment 
  assistant.fit_model() and assistant.save_model()

### Adding Functions

1. Go to `src/functions`.
2. Add a new file for your function.
3. Import the function in `sky_GUI.py`.
4. Modify `intents.json` to include your new intent.

After making changes, modify the section in `sky_GUI.py` related to model loading.

## Known Bugs and Issues

- Some functions may throw errors when called from `sky_GUI.py`.
- User responses for functions requiring interaction are currently fetched from the terminal; they should be fetched from the main GUI in `sky_GUI.py`.

Feel free to make necessary adjustments and improvements. Contributions are welcome!

```

Feel free to adapt this to your needs and project style.