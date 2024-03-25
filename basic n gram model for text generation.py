import random

def create_bigram_model(text):
    words = text.split()
    bigrams = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word in bigrams:
            bigrams[current_word].append(next_word)
        else:
            bigrams[current_word] = [next_word]
    return bigrams

def generate_text(bigrams, num_words=50):
    current_word = random.choice(list(bigrams.keys()))
    text = current_word
    for _ in range(num_words - 1):
        if current_word in bigrams:
            next_word = random.choice(bigrams[current_word])
            text += ' ' + next_word
            current_word = next_word
        else:
            break
    return text

# Example text
text = "The quick brown fox jumps over the lazy dog"

# Create bigram model
bigram_model = create_bigram_model(text)

# Generate text using the bigram model
generated_text = generate_text(bigram_model)
print(generated_text)
