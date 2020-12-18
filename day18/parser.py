import enum
import operator
import re

class TokenType(enum.Enum):
    T_NUM = 0
    T_PLUS = 1
    T_MULT = 2
    T_LPAR = 3
    T_RPAR = 4
    T_END = 5

operations = {
    TokenType.T_PLUS: operator.add,
    TokenType.T_MULT: operator.mul,
}

class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []


def lexical_analysis(s):
    mappings = {
        '+': TokenType.T_PLUS,
        '*': TokenType.T_MULT,
        '(': TokenType.T_LPAR,
        ')': TokenType.T_RPAR}

    tokens = []
    for c in s:
        if c in mappings:
            token_type = mappings[c]
            token = Node(token_type, value=c)
        elif re.match(r'\d', c):
            token = Node(TokenType.T_NUM, value=int(c))
        else:
            raise Exception('Invalid token: {}'.format(c))
        tokens.append(token)
    tokens = list(reversed(tokens))
    tokens.append(Node(TokenType.T_END))
    return tokens

def raise_syntax_error(self, tokens):
    raise Exception('Invalid syntax on token {}'.format(tokens[0].token_type))

def match(tokens, token):
    if tokens[0].token_type == token:
        return tokens.pop(0)
    else:
        raise_syntax_error(tokens)

class Parser:
    next_operators = set([TokenType.T_PLUS, TokenType.T_MULT, TokenType.T_LPAR, TokenType.T_END])

    def parse(self, input_string):
        tokens = lexical_analysis(input_string)
        ast = self.parse_expr(tokens)
        match(tokens, TokenType.T_END)
        return ast

    def parse_expr(self, tokens):
        return self.parse_rest(tokens, self.parse_node(tokens), [TokenType.T_PLUS, TokenType.T_MULT])

    def parse_rest(self, tokens, left_node, operators):
        operators = set(operators)
        if tokens[0].token_type in operators:
            node = tokens.pop(0)
            node.children.append(left_node)
            next_node = self.parse_expr(tokens)
            node.children.append(next_node)
            return node
        elif tokens[0].token_type in Parser.next_operators - operators:
            return left_node
        raise_syntax_error(tokens)

    def parse_node(self, tokens):
        if tokens[0].token_type == TokenType.T_NUM:
            return tokens.pop(0)
        match(tokens, TokenType.T_RPAR)
        e_node = self.parse_expr(tokens)
        match(tokens, TokenType.T_LPAR)
        return e_node

class Parser2(Parser):
    def parse_expr(self, tokens):
        return self.parse_rest(tokens, self.parse_precedence(tokens), [TokenType.T_MULT])

    def parse_precedence(self, tokens):
        return self.parse_plus(tokens, self.parse_node(tokens), [TokenType.T_PLUS])

    def parse_plus(self, tokens, left_node, operators):
        operators = set(operators)
        if tokens[0].token_type in [TokenType.T_PLUS]:
            node = tokens.pop(0)
            node.children.append(left_node)
            next_node = self.parse_precedence(tokens)
            node.children.append(next_node)
            return node
        elif tokens[0].token_type in Parser.next_operators - operators:
            return left_node
        raise_syntax_error(tokens)

def compute(node):
    if node.token_type == TokenType.T_NUM:
        return node.value
    left_result = compute(node.children[0])
    right_result = compute(node.children[1])
    operation = operations[node.token_type]
    return operation(left_result, right_result)

if __name__ == '__main__':
    data = open("input.txt", "r").readlines()
    total = 0
    parser = Parser()
    for line in data:
        ast = parser.parse(line.strip().replace(' ',''))
        total += compute(ast)
    print("Part 1:",total)
    parser = Parser2()
    for line in data:
        ast = parser.parse(line.strip().replace(' ',''))
        total += compute(ast)
    print("Part 2:",total)