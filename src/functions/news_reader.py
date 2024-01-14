import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
from news_extractor import extract_news_category

import sys
sys.path.append('AI-Assistant/src/')

from src.init import tts_instance

class NewsDisplay:
    def __init__(self, root):
        self.root = root
        self.image_references = []

    def show_page(self, current_page, news):
        for widget in self.root.winfo_children():
            widget.destroy()

        articles_per_page = 3
        start_index = (current_page - 1) * articles_per_page
        end_index = start_index + articles_per_page
        current_articles = news[start_index:end_index]

        for i, article in enumerate(current_articles):
            frame = ttk.Frame(self.root, padding="10")
            frame.grid(row=i, column=0, sticky="w")

            title_label = ttk.Label(frame, text=article['title'], font=('Arial', 14, 'bold'))
            title_label.grid(row=0, column=0, columnspan=2, sticky="w")

            img_url = article['urlToImage']
            if img_url:
                img_data = urlopen(img_url).read()
                img = Image.open(BytesIO(img_data))
                img.thumbnail((100, 100))
                photo = ImageTk.PhotoImage(img)
                label = ttk.Label(frame, image=photo)
                label.photo = photo  # Keep a reference to the image
                label.grid(row=1, column=0, rowspan=2, padx=10)

            description_label = ttk.Label(frame, text=article['description'], wraplength=400, justify="left")
            description_label.grid(row=1, column=1, sticky="w")

            frame.columnconfigure(0, weight=1)
            frame.columnconfigure(1, weight=1)

            def read_more(url):
                def open_url():
                    import webbrowser
                    webbrowser.open(url)
                return open_url

            read_more_button = ttk.Button(frame, text="Read More", command=read_more(article['url']))
            read_more_button.grid(row=2, column=1, sticky="w")

        prev_button = ttk.Button(self.root, text="Previous", command=lambda: self.show_page(current_page - 1, news))
        prev_button.grid(row=len(current_articles), column=0, sticky="w")

        next_button = ttk.Button(self.root, text="Next", command=lambda: self.show_page(current_page + 1, news))
        next_button.grid(row=len(current_articles), column=1, sticky="e")

    def on_closing(self):
        for img_ref in self.image_references:
            img_ref.__del__()

        self.root.destroy()

def display_news(news):
    root = tk.Tk()
    root.title("News Reader")

    news_display = NewsDisplay(root)
    root.protocol("WM_DELETE_WINDOW", news_display.on_closing)

    # Initialize the first page
    news_display.show_page(1, news)

    root.mainloop()

def get_news(q):
    api_key = "your_api_key"
    news_api_url = f'https://newsapi.org/v2/top-headlines?q={q}&apiKey={api_key}'

    response = requests.get(news_api_url)
    data = response.json()

    if response.status_code == 200 and data['status'] == 'ok':
        articles = data['articles']
        formatted_articles = [
            {
                'author': article['author'],
                'content': article['content'],
                'description': article['description'],
                'publishedAt': article['publishedAt'],
                'source': {
                    'id': article['source']['id'],
                    'name': article['source']['name']
                },
                'title': article['title'],
                'url': article['url'],
                'urlToImage': article['urlToImage']
            }
            for article in articles
        ]

        return formatted_articles
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")
        return []

def news_anchor(text):
    category = extract_news_category(text)
    if category is not None:
        news_data = get_news(category)
        tts_instance.speak(f"hold on as I fetch latest {category} news...")
        display_news(news_data)
    else:
        tts_instance.speak("try something like: fetch latest sports news")

if __name__ == "__main__":
    news_anchor("fetch tech news")
