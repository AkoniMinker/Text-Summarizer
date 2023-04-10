import tkinter as tk
from tkinter import scrolledtext
import spacy
from langdetect import detect
from heapq import nlargest
from collections import Counter


# Detect the language of the input text
def detect_language(text):
    try:
        language = detect(text)
    except:
        language = 'en'
    return language


def load_nlp_model(language):
    model_name = {
        'en': 'en_core_web_lg',
        'fr': 'fr_core_news_sm',
        'zh': 'zh_core_web_sm',
        'de': 'de_core_news_sm',
        'ja': 'ja_core_news_sm',
        'ko': 'ko_core_news_sm',
        'ru': 'ru_core_news_sm',
        'es': 'es_core_news_lg'
    }.get(language, 'en_core_web_lg')  # Default to English model if the language is not supported

    if getattr(sys, 'frozen', False):
        model_directory = os.path.join(sys._MEIPASS, model_name)
    else:
        model_directory = model_name

    try:
        nlp = spacy.load(model_directory)
    except OSError:
        import en_core_web_sm
        nlp = en_core_web_sm.load()

    return nlp


# Calculate the TF-IDF scores for each word in the document
def tf_idf(text, doc):
    # Filter out stop words and punctuation marks
    words = [token.text for token in doc if not token.is_stop and not token.is_punct]
    # Count the frequency of each word
    freqs = Counter(words)
    # Calculate the total number of words
    num_words = len(words)
    # Compute the term frequency (TF) scores
    tf_scores = {word: freq / num_words for word, freq in freqs.items()}

    # Compute the inverse document frequency (IDF) scores
    word_idfs = {}
    for word in set(words):
        word_idfs[word] = 1 + sum(1 for token in doc if token.text == word)

    idf_scores = {word: 1 / idf for word, idf in word_idfs.items()}

    # Calculate the final TF-IDF scores
    tf_idf_scores = {word: tf * idf_scores[word] for word, tf in tf_scores.items()}

    return tf_idf_scores


def main(user_text, num_sentences):
    language = detect_language(user_text)
    print(f"Detected language: {language}")

    nlp = load_nlp_model(language)

    summary = summarize_text_spacy(nlp, user_text, num_sentences)

    return summary


# Summarize the text using the SpaCy library
def summarize_text_spacy(nlp_model, text, num_sentences=3):
    # Parse the text
    doc = nlp_model(text)
    # Extract the sentences
    sentences = [sent for sent in doc.sents]
    # Calculate the TF-IDF scores
    tf_idf_scores = tf_idf(text, doc)

    # Rank the sentences based on their TF-IDF scores
    ranked_sentences = sorted(
        sentences,
        key=lambda x: sum(tf_idf_scores.get(token.text, 0) for token in x),
        reverse=True
    )
    # Select the top-ranked sentences for the summary
    top_sentences = nlargest(num_sentences, ranked_sentences)
    # Combine the selected sentences and return the summary
    return " ".join(str(s) for s in sorted(top_sentences, key=lambda s: s.start))


def summarize():
    user_text = input_text.get("1.0", tk.END).strip()
    num_sentences = int(num_sentences_entry.get())

    summary = main(user_text, num_sentences)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)


def create_ui():
    window = tk.Tk()
    window.title("Text Summarizer by Jaidin Hamilton")
    window.geometry("800x600")

    tk.Label(window, text="Enter the text you would like to summarize:").pack()

    global input_text
    input_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=10)
    input_text.pack()

    tk.Label(window, text="Enter the number of sentences for the summary:").pack()

    global num_sentences_entry
    num_sentences_entry = tk.Entry(window)
    num_sentences_entry.pack()

    tk.Button(window, text="Summarize", command=summarize).pack()

    tk.Label(window, text="Summary:").pack()

    global output_text
    output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=10)
    output_text.pack()

    window.mainloop()


def interactive_mode():
    print(r"""
    +-----------------------------------------------------------------------+
    |                                                                       |
    |      ✨     *       +   🌟       ⭐️            ✨    +   🌙     *    |
    |         '                    |                                        |
    |            ()    .-.,="``"=.    - o - 🚀                              |
    |   (                 _|          |_         🛰️    )                    |
    |*  o      *       (    `,           ,`    )    +         🌌  '         |
    |     +      +             (                 )        +        +        |
    |           ()                (               )    ()                   |
    |      +       +               (__)       (__)       +         +        |
    |                                                                       |
    |                          Text Summarizer                              |
    |                                                   by Jaidin Hamilton  |
    +-----------------------------------------------------------------------+
    """)
    while True:
        print("Please enter the text you would like to summarize:")
        print("Enter 'END' on a new line when you're done.")
        print("Enter 'EXIT' to exit the program.")

        user_text = []
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            elif line.strip().upper() == 'EXIT':
                return
            user_text.append(line)

        user_text = "\n".join(user_text)

        num_sentences = int(input("Enter the number of sentences for the summary: "))

        summary = main(user_text, num_sentences)

        print("\nSummary:")

        new_line_pref = input("Would you like each sentence on a new line? (y/n): ")
        if new_line_pref.lower() == 'y':
            for sentence in summary.split('. '):
                print(sentence.strip())
        else:
            print(summary)
        print("\n---\n")


if __name__ == "__main__":
    # Unhashtag to use interactive_mode()
    create_ui()
