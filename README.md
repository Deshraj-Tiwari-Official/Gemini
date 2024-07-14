# Gemini 💎 - Your Personal Assistant Bot

Gemini is a versatile Python-based personal assistant bot designed to help you with a wide range of tasks. Leveraging Natural Language Processing (NLP), Gemini can understand and respond to user queries, manage tasks, retrieve information, and much more.

## Features

- **Voice Interaction:** Understands and responds to voice commands.
- **Task Management:** Allows you to create, view, and manage to-do lists.
- **Information Retrieval:** Provides answers to general questions, latest news, and more.
- **Customizable Responses:** Tailor Gemini's responses to suit your needs.

## Installation

Follow these steps to set up Gemini on your local machine:

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Step-by-Step Guide

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Deshraj-Tiwari-Official/Gemini.git
    cd Gemini
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Add Your News API Key**

   Gemini requires a News API key to fetch the latest news headlines. Sign up at [NewsAPI](https://newsapi.org/) to get your API key. Then, add your API key to your environment variables or directly into the script where it's required.

    ```python
    NEWS_API = 'your_api_key_here'
    ```
   Create a .env file and add the api in the above format


4. **Run Gemini**

    ```bash
    python main.py
    ```

## Usage

Once you have started the bot, you can interact with Gemini through the command line or voice commands (if enabled).


### Voice Interaction

Gemini responds to voice commands. Simply speak your queries and wait for Gemini to respond.

### Adding Your Favorite Songs

To add your favorite songs to Gemini's library, edit the `song_library.py` file. Add your songs in the following format:

```python
songs = {
    "Despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "Shape of You": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    # Add more songs here
}
```

## [Command Cheatsheet](cheatsheet.md)

