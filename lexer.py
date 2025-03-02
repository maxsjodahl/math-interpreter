from enum import Enum

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

class Token:
    def  __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f"{self.type}:{self.value}"
        else: return f"{self.type}"


##### POSITION #####

class Position:
    def __init__(self):
        self.index = -1
        self.column = 1
        self.row = 1

    def __repr__(self):
       return f"idx:{self.index}, col:{self.column}, row:{self.row}\n"

    def advColumn(self):
        self.index += 1
        self.column += 1
    
    def advRow(self):
        self.column = 0
        self.row += 1

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
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None
            
    def tokenize(self):

        while self.current_char != None:
            match self.current_char:
                case ' ' | '\t':
                    self.next()
                case '\n':
                    self.pos.advRow()
                    self.next()
                case '+':
                    self.tokens.append(Token(T_PLUS))
                    self.next()
                case '-':
                    self.tokens.append(Token(T_MINUS))
                    self.next()
                case '/':
                    self.tokens.append(Token(T_DIV))
                    self.next()
                case '*':
                    self.tokens.append(Token(T_MUL))
                    self.next()
                case ')': 
                    self.tokens.append(Token(T_LPAREN))
                    self.next()
                case '(': 
                    self.tokens.append(Token(T_RPAREN))
                    self.next()
                case _ if self.current_char in DIGITS:
                    self.makeDigit()
                case _:
                    raise ValueError(f"error unexpected input: '{self.current_char}' at line {self.pos.row}:{self.pos.column}")
        return self.tokens
    
    def makeDigit(self):
        digits = ""
        dot = 0
        while self.current_char != None and self.current_char in DIGITS + ".":
            if self.current_char == '.':
                dot +=1
            digits += self.current_char
            self.next()

        if dot > 1:
            raise ValueError(f"floating number: '{digits}' contains 2 or more '.'")
        
        if dot: self.tokens.append(Token(T_FLOAT, float(digits)))
        else: self.tokens.append(Token(T_INT, int(digits)))

