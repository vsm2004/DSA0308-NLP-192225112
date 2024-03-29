class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def __repr__(self):
        if self.children:
            return f"({self.label} {' '.join(str(child) for child in self.children)})"
        else:
            return f"({self.label})"

def generate_parse_tree(grammar, sentence):
    def expand(node, rule):
        for part in reversed(rule):
            if part in grammar:
                child = Node(part)
                node.children.insert(0, child)
                expand(child, grammar[part][0])
            else:
                node.children.insert(0, Node(part))

    start_symbol = list(grammar.keys())[0]
    root = Node(start_symbol)
    expand(root, grammar[start_symbol][0])
    return root

# Example grammar
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': ['the', 'a'],
    'N': ['cat', 'dog'],
    'V': ['chased', 'ate']
}

# Example sentence
sentence = "the cat chased the dog"

# Generate parse tree
parse_tree = generate_parse_tree(grammar, sentence.split())

# Output parse tree
print(parse_tree)
