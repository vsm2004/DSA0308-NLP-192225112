class PluralMachine:
    def __init__(self):
        self.current_state = 'q0'  # Initial state
        self.final_state = 'q2'    # Final state
        self.transitions = {
            'q0': {'singular': 'q1'},
            'q1': {'noun': 'q2'}
        }
        self.irregular_nouns = {
            'child': 'children',
            'person': 'people',
            'ox': 'oxen',
            'goose': 'geese'
        }

    def generate_plural(self, noun):
        # Check for irregular nouns
        if noun in self.irregular_nouns:
            return self.irregular_nouns[noun]
        
        # Initialize plural form with default rules
        plural_form = noun + 's'
        
        # Apply FSM rules if needed
        if self.current_state == 'q0':
            self.current_state = self.transitions[self.current_state]['singular']
        elif self.current_state == 'q1':
            self.current_state = self.transitions[self.current_state]['noun']

        # Check if the current state is the final state
        if self.current_state == self.final_state:
            return plural_form
        else:
            return "Error: Invalid noun or plural form generation."

# Example usage
plm = PluralMachine()
nouns = ['cat', 'dog', 'child', 'person', 'ox', 'goose']
for noun in nouns:
    plural = plm.generate_plural(noun)
    print(f"Singular: {noun}, Plural: {plural}")
