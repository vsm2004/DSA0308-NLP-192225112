import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample text for morphological analysis
text = "cats running ran cactus cacti better best"

# Tokenize the text into words
words = word_tokenize(text)

# Perform morphological analysis (lemmatization) on each word
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Print the lemmatized words
print("Original words:", words)
print("Lemmatized words:", lemmatized_words)
