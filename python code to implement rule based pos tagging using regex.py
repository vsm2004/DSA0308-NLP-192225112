import re

# Define regular expression patterns for POS tagging rules
patterns = [
    (r'\b[A-Z][a-z]*\b', 'NNP'),  # Proper nouns
    (r'\b(?:[A-Z]\.)+[A-Z]?\.?\b', 'NNP'),  # Abbreviations like U.S.A., Mr., Mrs.
    (r'\b(?:[A-Za-z]+\.)+[A-Za-z]+\b', 'NNP'),  # Full names like John F. Kennedy
    (r'\b(?:[A-Za-z]+\.)+[A-Z]\b', 'NNP'),  # Abbreviated names like J. Smith
    (r'\b(?:[A-Za-z]+\-[A-Za-z]+)+\b', 'NN'),  # Hyphenated words like mother-in-law
    (r'\b\d+\b', 'CD'),  # Cardinal numbers
    (r'\b[a-zA-Z]+\b', 'NN'),  # Nouns (default)
    (r'\b(?:is|am|are|was|were|be|being|been)\b', 'VB'),  # Verbs
    (r'\b(?:in|on|at|by|with|for|of|to|over|under|above|below|near|before|after)\b', 'IN'),  # Prepositions
    (r'\b(?:the|a|an)\b', 'DT'),  # Determiners
    (r'\b(?:and|or|but|not)\b', 'CC'),  # Coordinating conjunctions
    (r'\b(?:is|am|are|was|were|be|being|been)\b', 'VB'),  # Verbs
    (r'\b(?:can|could|will|would|shall|should|may|might|must)\b', 'MD'),  # Modal verbs
    (r'\b(?:I|me|my|mine|you|your|yours|he|him|his|she|her|hers|it|its|we|us|our|ours|they|them|their|theirs)\b', 'PRP'),  # Personal pronouns
    (r'\b(?:this|that|these|those|which|who|whom|whose|what|when|where|why|how)\b', 'WDT'),  # Wh-determiners
    (r'\b(?:because|if|while|since|although|though|until|unless|than|as)\b', 'IN'),  # Subordinating conjunctions
    (r'\b(?:to|into|up|down|off|out|over)\b', 'RP'),  # Particles
    (r'\b(?:very|too|so|enough)\b', 'RB'),  # Adverbs
    (r'\b(?:good|great|nice|happy|sad|angry|beautiful|ugly|smart|dumb)\b', 'JJ'),  # Adjectives
    (r'\b(?:and|or|but|not)\b', 'CC'),  # Coordinating conjunctions
    (r'\b(?:for|against|with)\b', 'IN'),  # Complex prepositions
]

# Function to perform rule-based POS tagging
def rule_based_pos_tagging(sentence, patterns):
    tagged_sentence = []
    for word in sentence:
        tagged_word = None
        for pattern, tag in patterns:
            if re.fullmatch(pattern, word):
                tagged_word = (word, tag)
                break
        if tagged_word is None:
            tagged_word = (word, 'NN')  # Default to noun if no match found
        tagged_sentence.append(tagged_word)
    return tagged_sentence

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
words = re.findall(r'\b\w+\b', sentence)  # Tokenize the sentence into words
tagged_sentence = rule_based_pos_tagging(words, patterns)
print("Rule-Based POS Tagging Result:", tagged_sentence)
