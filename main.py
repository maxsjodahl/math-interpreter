import sys
from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter


while True:
    try:
        text = input("> ")
        # text = "2+3*5"
        lex = Lexer(text)
        tokens = lex.tokenize()
        print(f"{tokens}")

        pars = Parser(tokens)
        ast = pars.parse()
        print(f'{ast}')

        inter = Interpreter(ast)
        result = inter.run()
        print(f'{text} = {result}')

    except Exception as e:
        # print the error without the traceback
        print(e, file=sys.stderr)
