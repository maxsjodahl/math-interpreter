from src.createErrorText import CustomError
##### DIGITS #####

DIGITS = "0123456789"

##### TOKENS #####

T_INT = "INT"
T_FLOAT = "FLOAT"
T_PLUS = "PLUS"
T_MINUS = "MINUS"
T_DIV = "DIV"
T_MUL = "MUL"
T_LPAREN = "LPAREN"
T_RPAREN = "RPAREN"

T_SEP = "SEP"
T_EOF = "EOF"


##### TOKEN #####


class Token:
    def __init__(self, type_, position, value=None):
        self.type = type_
        self.position = position
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        else:
            return f"{self.type}"


##### POSITION #####


class Position:
    def __init__(self, idx=-1, col=-1, row=0):
        self.index = idx
        self.column = col
        self.row = row

    def __repr__(self):
        return f"idx:{self.index}, col:{self.column}, row:{self.row}\n"

    def advColumn(self):
        self.index += 1
        self.column += 1

    def advRow(self):
        self.column = -1
        self.row += 1

    ### Might want in the future, dont know yet
    def copy(self):
        return Position(self.index, self.column, self.row)


##### LEXER #####


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = Position()
        self.tokens = []
        self.current_char = None
        self.next()

    def next(self):
        self.pos.advColumn()
        self.current_char = (
            self.text[self.pos.index] if self.pos.index < len(self.text) else None
        )

    def tokenize(self):
        while self.current_char is not None:
            match self.current_char:
                case " " | "\t":
                    self.next()
                case "\n":
                    self.tokens.append(Token(T_SEP, self.pos.copy()))
                    self.pos.advRow()
                    self.next()
                case "+":
                    self.tokens.append(Token(T_PLUS, self.pos.copy()))
                    self.next()
                case "-":
                    self.tokens.append(Token(T_MINUS, self.pos.copy()))
                    self.next()
                case "/":
                    self.tokens.append(Token(T_DIV, self.pos.copy()))
                    self.next()
                case "*":
                    self.tokens.append(Token(T_MUL, self.pos.copy()))
                    self.next()
                case ")":
                    self.tokens.append(Token(T_RPAREN, self.pos.copy()))
                    self.next()
                case "(":
                    self.tokens.append(Token(T_LPAREN, self.pos.copy()))
                    self.next()
                case _ if self.current_char in DIGITS:
                    err = self.makeDigit()
                    if err is not None:
                        return None, err
                case _:
                    raise CustomError(
                        f"error unexpected input: '{self.current_char}' at line {self.pos.row + 1}:{self.pos.column}",
                        self.pos.copy(),
                    )
        self.tokens.append(Token(T_EOF, self.pos.copy()))
        return self.tokens, None

    def makeDigit(self):
        digits = ""
        dot = 0
        pos = self.pos.copy()
        while self.current_char is not None and self.current_char in DIGITS + ".":
            if self.current_char == ".":
                dot += 1
            digits += self.current_char
            self.next()

        if dot > 1:
            raise CustomError(
                f"floating number: '{digits}' contains 2 or more '.'", pos
            )

        if dot:
            self.tokens.append(Token(T_FLOAT, pos, float(digits)))
        else:
            self.tokens.append(Token(T_INT, pos, int(digits)))
