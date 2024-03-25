import nltk
from nltk.tokenize import word_tokenize

# Sample text for POS tagging
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
words = word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = nltk.pos_tag(words)

# Print the POS tags for each word
print("Original Text:", text)
print("POS Tags:", pos_tags)
