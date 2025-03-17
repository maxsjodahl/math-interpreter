from lexer import Lexer
from parser import Parser


while True:
    text = input("> ")
    # text = "2+3*5"
    lex = Lexer(text)
    pars = Parser(text)
    try:
        tokens = lex.tokenize()
        print(f"{tokens}")
        ast = pars.parse()
        print(f'{ast}')
    except Exception as e:
        print(f"{e}")
        break
