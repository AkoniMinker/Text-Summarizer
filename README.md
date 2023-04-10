# Text Summarizer

Text Summarizer is a simple Python application that uses the SpaCy library and the langdetect library to summarize large chunks of text into a smaller, more concise version. The user can choose the number of sentences they would like in the summary.

## Features

- Detects the language of the input text
- Supports multiple languages (English, French, Chinese, German, Japanese, Korean, Russian, and Spanish)
- Summarizes the text using the SpaCy library
- GUI interface for easy interaction

## Requirements

- Python 3.6 or higher
- SpaCy library (version 3.x)
- langdetect library
- tkinter library (should be included in Python 3.1+ by default)

## Installation

1. Clone the repository or download the source code.

2. Set up a virtual environment (optional but recommended):

   python -m venv venv

3. Activate the virtual environment:

   - On Windows:

     venv\Scripts\activate

   - On Linux/Mac:

     source venv/bin/activate

4. Install the required packages:

   pip install -r requirements.txt

5. Download the necessary SpaCy models:

   python -m spacy download en_core_web_lg
   python -m spacy download fr_core_news_sm
   python -m spacy download zh_core_web_sm
   python -m spacy download de_core_news_sm
   python -m spacy download ja_core_news_sm
   python -m spacy download ko_core_news_sm
   python -m spacy download ru_core_news_sm
   python -m spacy download es_core_news_lg

## Usage

Run the Text Summarizer application:

Download the .exe file (64,404 KB) here >> https://drive.google.com/file/d/1fQkApOyaqBWbEaeFfruhE1ZkIr696Dj7/view?usp=sharing

A graphical interface will appear. Enter the text you would like to summarize and the desired number of sentences for the summary. Then, click the "Summarize" button to generate the summary.
