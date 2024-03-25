# Define transformation rules as a dictionary where keys are words and values are POS tags
transformation_rules = {
    "quick": "JJ",  # Adjective
    "brown": "JJ",  # Adjective
    "fox": "NN",    # Noun
    "jumps": "VBZ",  # Verb
    "over": "IN",   # Preposition
    "the": "DT",    # Determiner
    "lazy": "JJ",   # Adjective
    "dog": "NN"     # Noun
}

# Function to apply transformation rules and tag words
def transform_based_tagging(sentence, transformation_rules):
    tagged_sentence = []
    for word in sentence:
        if word in transformation_rules:
            pos_tag = transformation_rules[word]
        else:
            pos_tag = "UNKNOWN"  # Default to UNKNOWN if word not in rules
        tagged_sentence.append((word, pos_tag))
    return tagged_sentence

# Example usage
sentence = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
tagged_sentence = transform_based_tagging(sentence, transformation_rules)
print("Transformation-Based Tagging Result:", tagged_sentence)
