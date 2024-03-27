import re

class Parser:
    def __init__(self, input_string):
        self.tokens = re.findall(r'\d+|\+|-|\*|/|\(|\)', input_string)
        self.index = 0

    def match(self, token):
        if self.index < len(self.tokens) and self.tokens[self.index] == token:
            self.index += 1
        else:
            raise SyntaxError(f"Expected '{token}' but found '{self.tokens[self.index]}'")

    def expr(self):
        self.term()
        while self.index < len(self.tokens) and self.tokens[self.index] in ('+', '-'):
            print(self.tokens[self.index])  # Output the operator
            self.index += 1
            self.term()

    def term(self):
        self.factor()
        while self.index < len(self.tokens) and self.tokens[self.index] in ('*', '/'):
            print(self.tokens[self.index])  # Output the operator
            self.index += 1
            self.factor()

    def factor(self):
        if self.index < len(self.tokens):
            if self.tokens[self.index].isdigit():
                print(self.tokens[self.index])  # Output the number
                self.index += 1
            elif self.tokens[self.index] == '(':
                print(self.tokens[self.index])  # Output the opening parenthesis
                self.index += 1
                self.expr()
                self.match(')')
                print(')')  # Output the closing parenthesis
            else:
                raise SyntaxError(f"Unexpected token '{self.tokens[self.index]}'")
        else:
            raise SyntaxError("Unexpected end of input")

    def parse(self):
        self.expr()
        if self.index == len(self.tokens):
            print("Parsing successful!")
        else:
            raise SyntaxError("Unexpected tokens at the end of input")

# Example usage
input_string = "3+(4*2)-1"
parser = Parser(input_string)
parser.parse()

