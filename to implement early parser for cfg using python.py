class EarleyItem:
    def __init__(self, production, dot_index, start_index):
        self.production = production  # A production from the grammar
        self.dot_index = dot_index  # Position of the dot in the production
        self.start_index = start_index  # Start index in the input string

    def __eq__(self, other):
        return (
            self.production == other.production
            and self.dot_index == other.dot_index
            and self.start_index == other.start_index
        )

    def __hash__(self):
        return hash((self.production, self.dot_index, self.start_index))

def earley_parse(grammar, input_string):
    chart = [[] for _ in range(len(input_string) + 1)]
    start_production = grammar[0]  # Assume the first production is the start production
    start_item = EarleyItem(start_production, 0, 0)
    chart[0].append(start_item)

    for i in range(len(input_string) + 1):
        for item in chart[i]:
            if item.dot_index < len(item.production) and is_nonterminal(item.production[item.dot_index]):
                predict(grammar, chart, item)
            elif item.dot_index < len(item.production) and item.production[item.dot_index] == input_string[i]:
                scan(chart, item, input_string[i], i)
            elif item.dot_index == len(item.production):
                complete(chart, item)

    return start_item in chart[len(input_string)]

def is_nonterminal(symbol):
    # Implement your logic to check if a symbol is a nonterminal
    return symbol.isupper()

def predict(grammar, chart, item):
    next_symbol = item.production[item.dot_index]
    for production in grammar:
        if production[0] == next_symbol:
            new_item = EarleyItem(production, 0, item.start_index)
            if new_item not in chart[item.start_index]:
                chart[item.start_index].append(new_item)

def scan(chart, item, symbol, position):
    new_item = EarleyItem(item.production, item.dot_index + 1, item.start_index)
    if new_item not in chart[position + 1]:
        chart[position + 1].append(new_item)

def complete(chart, item):
    for entry in chart[item.start_index]:
        if entry.dot_index < len(entry.production) and entry.production[entry.dot_index] == item.production[0]:
            new_item = EarleyItem(entry.production, entry.dot_index + 1, entry.start_index)
            if new_item not in chart[item.start_index + 1]:
                chart[item.start_index + 1].append(new_item)

# Example usage
grammar = [
    ('S', ['NP', 'VP']),
    ('NP', ['Det', 'N']),
    ('NP', ['NP', 'PP']),
    ('VP', ['V', 'NP']),
    ('VP', ['VP', 'PP']),
    ('PP', ['P', 'NP']),
    ('Det', ['the']),
    ('Det', ['a']),
    ('N', ['man']),
    ('N', ['woman']),
    ('V', ['saw']),
    ('P', ['with']),
]

input_string = 'the man saw a woman with a telescope'

print(earley_parse(grammar, input_string))
