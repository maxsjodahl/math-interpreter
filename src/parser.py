import src.lexer as lexer


##### PARSER NODES #####

class NumberNode:
    def __init__(self, token):
        self.token: lexer.Token = token

    def __repr__(self):
        return f'{self.token}'

class UnaryNode:
    def __init__(self, s_token, v_token):
        self.s_token = s_token
        self.v_token = v_token

    def __repr__(self):
        return f'({self.s_token}, {self.v_token})'

class BinaryNode:
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op: lexer.Token = op

    def __repr__(self):
        return f'({self.left}, {self.op}, {self.right})'

##### PARSER #####

class Parser:

# expr : term ((PLUS|MINUS) term)*

# term : factor ((MUL|DIV) factor)*

# factor : INT|FLOAT
#        | (MINUS|PLUS) INT|FLOAT


    def __init__(self, text):
        self.tokens: list[lexer.Token] = lexer.Lexer(text).tokenize()
        self.index = -1
        self.advance()

    def advance(self):
        self.index +=1

        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        return self.current_token


    def parse(self):
        result = self.expr()
        return result

    def factor(self):
        token = self.current_token

        if token.type in [lexer.T_INT, lexer.T_FLOAT]:
            self.advance()
            return NumberNode(token)

        elif token.type in [lexer.T_MINUS, lexer.T_PLUS]:
            self.advance()
            v_token = self.current_token
            self.advance()
            return UnaryNode(token, v_token)

        elif token.type in [lexer.T_LPAREN]:
            self.advance()
            expr = self.expr()

            if self.current_token.type in [lexer.T_RPAREN]:
                self.advance()
                return expr
            else:
                raise ValueError ("error: expected ')'")

    def term(self):
        left = self.factor()

        while self.current_token.type in [lexer.T_MUL, lexer.T_DIV]:
            op_token = self.current_token
            self.advance()
            right = self.factor()
            left = BinaryNode(left, op_token, right)

        return left

    def expr(self):
        left = self.term()

        while self.current_token.type in [lexer.T_PLUS, lexer.T_MINUS]:
            op_token = self.current_token
            self.advance()
            right = self.term()
            left = BinaryNode(left, op_token, right)

        return left

