import nltk

# Define a probabilistic context-free grammar (PCFG)
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | V [0.3]
    NP -> Det N [0.6] | N [0.4]
    V -> "saw" [1.0]
    N -> "man" [0.5] | "telescope" [0.5]
    Det -> "the" [1.0]
""")

# Create a parser with the defined PCFG
parser = nltk.ViterbiParser(grammar)

# Define a sentence to parse
sentence = "the man saw the telescope".split()

# Parse the sentence and print the most probable parse tree
for tree in parser.parse(sentence):
    print(tree)
