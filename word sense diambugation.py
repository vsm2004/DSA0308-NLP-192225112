from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lesk_algorithm(word, sentence):
    best_sense = None
    max_overlap = 0
    context = set(word_tokenize(sentence.lower()))
    context = context.difference(set(stopwords.words('english')))  # Remove stopwords

    for synset in wordnet.synsets(word):
        signature = set(word_tokenize(synset.definition().lower()))
        signature.update([word.lower() for word in synset.lemma_names()])  # Include lemma names
        signature = signature.difference(set(stopwords.words('english')))  # Remove stopwords

        overlap = len(context.intersection(signature))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = synset

    return best_sense

# Example usage
word = "bank"
sentence = "I went to the bank to deposit my money."

sense = lesk_algorithm(word, sentence)
if sense:
    print("Word:", word)
    print("Sentence:", sentence)
    print("Best sense:", sense)
    print("Definition:", sense.definition())
else:
    print("No sense found for the word '{}' in the given sentence.".format(word))
