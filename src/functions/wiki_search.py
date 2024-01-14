import wikipediaapi
import tkinter as tk
from src.init import tts_instance
import threading
import time

class WikipediaSearchGUI:
    def __init__(self, query):
        self.query = query
        self.stop_speaking = False

        # Create Tkinter window
        self.root = tk.Tk()
        self.root.title("Wikipedia Summary")

        # Create a label to display the summary
        summary_text = self.get_summary_text()
        self.summary_label = tk.Label(self.root, text=summary_text, wraplength=400, justify="left")
        self.summary_label.pack(padx=10, pady=10)

        # Button to close the window
        self.close_button = tk.Button(self.root, text="Close", command=self.close_window)
        self.close_button.pack(pady=10)

        # Create a thread to run the speak_summary function
        self.speak_thread = threading.Thread(target=self.speak_summary)
        self.speak_thread.start()

        # Run the Tkinter main loop
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.mainloop()

    def close_window(self):
        self.stop_speaking = True  # Signal to stop speaking
        self.root.destroy()

    def speak_summary(self):
        first_paragraph = self.get_first_paragraph()
        while not self.stop_speaking and first_paragraph:
            try:
                tts_instance.speak(first_paragraph)
                time.sleep(0.5)  # Adjust the sleep duration as needed
            except RuntimeError:
                tts_instance.speak("I cannot read this file. It's large")

    def get_first_paragraph(self):
        wiki_wiki = wikipediaapi.Wikipedia('skyAI/0.1')
        page_py = wiki_wiki.page(self.query)
        return page_py.text.split('\n\n')[0] if page_py.exists() else ""

    def get_summary_text(self):
        return f"Summary for {self.query}:\n\n{self.get_first_paragraph()}"

# Example usage
# query_to_search = "james gosling"
# wikipedia_gui = WikipediaSearchGUI(query_to_search)
