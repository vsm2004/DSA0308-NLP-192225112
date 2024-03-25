import random

# Sample text for training the probabilistic model
training_data = [
    ("The", "DT"), ("quick", "JJ"), ("brown", "JJ"), ("fox", "NN"),
    ("jumps", "VBZ"), ("over", "IN"), ("the", "DT"), ("lazy", "JJ"), ("dog", "NN")
]

# Function to train the probabilistic model
def train_probabilistic_model(training_data):
    word_pos_freq = {}
    pos_transitions = {}
    
    for i in range(len(training_data)):
        word, pos = training_data[i]
        
        # Count frequency of each word with its POS tag
        if word in word_pos_freq:
            if pos in word_pos_freq[word]:
                word_pos_freq[word][pos] += 1
            else:
                word_pos_freq[word][pos] = 1
        else:
            word_pos_freq[word] = {pos: 1}
        
        # Count transitions between POS tags
        if i < len(training_data) - 1:
            next_pos = training_data[i + 1][1]
            if pos in pos_transitions:
                if next_pos in pos_transitions[pos]:
                    pos_transitions[pos][next_pos] += 1
                else:
                    pos_transitions[pos][next_pos] = 1
            else:
                pos_transitions[pos] = {next_pos: 1}
    
    # Normalize frequencies to probabilities
    for word in word_pos_freq:
        total_count = sum(word_pos_freq[word].values())
        word_pos_freq[word] = {pos: freq / total_count for pos, freq in word_pos_freq[word].items()}
    
    for pos in pos_transitions:
        total_count = sum(pos_transitions[pos].values())
        pos_transitions[pos] = {next_pos: freq / total_count for next_pos, freq in pos_transitions[pos].items()}
    
    return word_pos_freq, pos_transitions

# Train the probabilistic model
word_pos_freq, pos_transitions = train_probabilistic_model(training_data)

# Function to perform stochastic POS tagging
def stochastic_pos_tagging(sentence, word_pos_freq, pos_transitions):
    tagged_sentence = []
    prev_pos = None
    
    for word in sentence:
        if word in word_pos_freq:
            pos_probs = word_pos_freq[word]
            pos = random.choices(list(pos_probs.keys()), weights=list(pos_probs.values()))[0]
        else:
            pos = "NN"  # Default to noun if word not in training data
        
        if prev_pos and prev_pos in pos_transitions:
            next_pos_probs = pos_transitions[prev_pos]
            next_pos = random.choices(list(next_pos_probs.keys()), weights=list(next_pos_probs.values()))[0]
        else:
            next_pos = "END"  # Default to end of sentence
        
        tagged_sentence.append((word, pos))
        prev_pos = next_pos
    
    return tagged_sentence

# Example usage
sentence = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
tagged_sentence = stochastic_pos_tagging(sentence, word_pos_freq, pos_transitions)
print("Stochastic POS Tagging Result:", tagged_sentence)
