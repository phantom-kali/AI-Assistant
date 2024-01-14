import tkinter as tk
from tkinter import scrolledtext, messagebox
import speech_recognition as sr
from neuralintents import BasicAssistant
from functions.media_coodinator import play_video_now, play_music_now
from functions.core import find_word_meaning
from functions.core import google_search, wiki_search
from functions.news_reader import news_anchor
from functions.jokes_app import get_joke
from functions.fun_game import play_number_guessing_game
from functions.core import terminate
from init import tts_instance

import logging

mappings = {
    'play music': play_music_now,
    'play video': play_video_now,
    'word meaning': find_word_meaning,
    'google search': google_search,
    'wiki search': wiki_search,
    'read news': news_anchor,
    'tell joke': get_joke,
    'play game': play_number_guessing_game,
    'terminate': terminate
}

assistant = BasicAssistant("src/data/intents.json", mappings, model_name="sky")

logging.basicConfig(filename='src/logs/conversation.log',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# assistant.fit_model()
# assistant.save_model()
assistant.load_model()

tts_instance.speak("Session Started")


class ChatGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat Application")

        # Create a frame for chat history
        chat_frame = tk.Frame(self.root)
        chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create scrolled text widget for chat history
        self.chat_history = scrolledtext.ScrolledText(chat_frame, width=50, height=20, state=tk.DISABLED, wrap=tk.WORD,
                                                      font=("Helvetica", 12))
        self.chat_history.pack(fill=tk.BOTH, expand=True)

        # Create a frame for user input and send button
        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create entry widget for user input
        self.message_entry = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Create send button
        self.send_button = tk.Button(input_frame, text="Send", command=self.send_message, font=("Helvetica", 12),
                                     bg="#0088cc", fg="white", relief=tk.GROOVE)
        self.send_button.pack(side=tk.RIGHT)

        # Create speech button
        self.speech_button = tk.Button(input_frame, text="Speech", command=self.activate_speech, font=("Helvetica", 12),
                                       bg="#4CAF50", fg="white", relief=tk.GROOVE)
        self.speech_button.pack(side=tk.RIGHT, padx=(0, 10))

        # Configure tags for different sides of the chat
        self.chat_history.tag_configure('user', justify='left', foreground='blue')
        self.chat_history.tag_configure('assistant', justify='right', foreground='green')

        # Bind return key to send_message function
        self.root.bind('<Return>', lambda event=None: self.send_message())

        # Initialize speech recognition
        self.recognizer = sr.Recognizer()

    def send_message(self):
        user_input = self.message_entry.get().strip()
        if user_input:
            # Disable input field and change button text during processing
            self.message_entry.config(state=tk.DISABLED)
            self.send_button.config(text="Processing...", state=tk.DISABLED)
            self.root.update_idletasks()  # Force GUI update

            logging.info(f'User: {user_input}')

            result = assistant.process_input(user_input)


            if result:
                intent, response = result

                if intent:
                    logging.info(f'Intent: {intent}')

                if response != "200":
                    logging.info(f'Response: {response}')
                    self.display_message(f'You: {user_input}', sender='user')  # Fix sender parameter

                    # Display the assistant's response
                    self.display_message(f'Sky: {response}', sender='assistant')

                    tts_instance.speak(response)

                elif response is None and intent is None:
                    self.display_message(f'You: {user_input}', sender='user')
                    self.display_message("Sky: try rephrasing your request", sender='assistant')
                    tts_instance.speak("Sky: try rephrasing your request")

                else:
                    self.display_message(f'You: {user_input}', sender='user')
                    self.display_message(f'Sky: executing...', sender='assistant')

            else:
                self.display_message(f'You: {user_input}', sender='user')
                self.display_message("Sky: unusual computation error occurred", sender='assistant')
                tts_instance.speak("unusual computation error occurred")

            # Enable input field and reset button text after processing
            self.message_entry.config(state=tk.NORMAL)
            self.send_button.config(text="Send", state=tk.NORMAL)
            self.root.update_idletasks()  # Force GUI update

            self.message_entry.delete(0, tk.END)  # Clear the input field

    def display_message(self, message, sender='user'):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, message + '\n', sender)
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.see(tk.END)  # Scroll to the end

    def activate_speech(self):
        # Change the text of the speech button to indicate listening
        self.speech_button.config(text="Listening...", state=tk.DISABLED)
        self.root.update_idletasks()  # Force GUI update

        try:
            with sr.Microphone() as source:
                audio = self.recognizer.listen(source, timeout=0.5)
                user_input = self.recognizer.recognize_google(audio)
                self.message_entry.delete(0, tk.END)
                self.message_entry.insert(0, user_input)
                self.send_message()  # Call send_message to process the speech input
        except sr.UnknownValueError:
            self.display_message("Sorry, I couldn't understand what you said.", sender='assistant')
        except sr.RequestError:
            self.display_message("Sorry, there was an error with the speech recognition service.", sender='assistant')
        finally:
            # Change the text of the speech button back to "Speech"
            self.speech_button.config(text="Speech", state=tk.NORMAL)
            self.root.update_idletasks()  # Force GUI update


    def run(self):
        self.root.mainloop()


# Create an instance of the ChatGUI class and run the application
chat_gui = ChatGUI()
chat_gui.run()
