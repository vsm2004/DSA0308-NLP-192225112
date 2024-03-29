import nltk

def check_agreement(sentence, grammar_rules):
    parser = nltk.ChartParser(grammar_rules)
    try:
        parsed_trees = list(parser.parse(sentence.split()))
        if parsed_trees:
            return True
        else:
            return False
    except ValueError:
        return False

def main():
    # Define your context-free grammar rules
    grammar_rules = nltk.CFG.fromstring("""
        S -> NP VP
        NP -> Det N
        VP -> V
        Det -> 'the' | 'a'
        N -> 'cat' | 'dog'
        V -> 'runs' | 'barks'
    """)

    # Test sentences
    sentences = [
        "the cat runs",
        "a dog barks",
        "the dog runs",
        "a cat barks",
        "the cat barks",  # Incorrect sentence
        "a dog runs",     # Incorrect sentence
    ]

    for sentence in sentences:
        if check_agreement(sentence, grammar_rules):
            print(f"'{sentence}' agrees with the grammar rules.")
        else:
            print(f"'{sentence}' does not agree with the grammar rules.")

if __name__ == "__main__":
    main()
