import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Initialize the Porter Stemmer
porter_stemmer = PorterStemmer()

# Sample list of words for stemming
words = ["running", "ran", "cats", "dogs", "better", "best", "programming", "programmer"]

# Perform stemming on each word
stemmed_words = [porter_stemmer.stem(word) for word in words]

# Print the original words and their stemmed forms
for original, stemmed in zip(words, stemmed_words):
    print(f"Original: {original}, Stemmed: {stemmed}")
