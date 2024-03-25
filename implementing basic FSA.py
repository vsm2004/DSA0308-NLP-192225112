class FSA:
    def __init__(self):
        self.current_state = 'q0'  
        self.final_state = 'q2'    
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q1', 'b': 'q0'}
        }

    def process_input(self, input_string):
        for symbol in input_string:
            if symbol not in self.transitions[self.current_state]:
                return False  
            self.current_state = self.transitions[self.current_state][symbol]
        return self.current_state == self.final_state
fsa = FSA()
input_strings = ['aab', 'abb', 'abab', 'abc', 'ba']
for string in input_strings:
    if fsa.process_input(string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")
