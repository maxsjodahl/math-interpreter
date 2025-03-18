import sys
from src.lexer import Lexer
from src.parser import Parser


while True:
    try:
        text = input("> ")
        # text = "2+3*5"
        lex = Lexer(text)
        pars = Parser(text)

        tokens = lex.tokenize()
        print(f"{tokens}")
        ast = pars.parse()
        print(f'{ast}')

    except Exception as e:
        # print the error without the traceback
        print(e, file=sys.stderr)
