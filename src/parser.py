import src.lexer as lexer


##### PARSER NODES #####
class ExpressionNode:
    def __init__(self):
        pass


class NumberNode:
    def __init__(self, token):
        self.token: lexer.Token = token

    def __repr__(self):
        return f"{self.token}"


class UnaryNode:
    def __init__(self, s_token, v_token):
        self.s_token = s_token
        self.v_token = v_token

    def __repr__(self):
        return f"({self.s_token}, {self.v_token})"


class BinaryNode:
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op: lexer.Token = op

    def __repr__(self):
        return f"({self.left}, {self.op}, {self.right})"


##### PARSER #####


class Parser:
    # expr : term ((PLUS|MINUS) term)*

    # term : factor ((MUL|DIV) factor)*

    # factor : INT|FLOAT
    #        | (MINUS|PLUS) INT|FLOAT

    def __init__(self, tokens):
        self.tokens: list[lexer.Token] = tokens
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1

        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        return self.current_token

    def parse(self):
        result = [self.expr()]
        if self.current_token.type in [lexer.T_SEP]:
            self.advance()
            result.append(self.expr())
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
                raise ValueError("error: expected ')'")
        elif token.type in [lexer.T_EOF]:
            raise ValueError("factor error: EOF")

    def term(self):
        return self.op_helper(self.factor, [lexer.T_MUL, lexer.T_DIV])

    def expr(self):
        return self.op_helper(self.term, [lexer.T_PLUS, lexer.T_MINUS])

    def op_helper(self, func, list):
        left = func()

        while self.current_token.type in list:
            op_token = self.current_token
            self.advance()
            right = func()
            left = BinaryNode(left, op_token, right)

        if self.current_token.type in [lexer.T_INT, lexer.T_FLOAT]:
            raise SyntaxError("syntax error: expected EOF")

        return left
