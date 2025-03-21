import sys
import re
from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter
from src.createErrorText import CustomError, ErrorText


# while True:
try:
    # text = input("> ")
    text = "     1+3 *5.0+1.1 + 5\n5+(5*3+59.00+1)"
    errorText = ErrorText(text)
    # text = "2+3*5"
    lex = Lexer(text)
    tokens, error = lex.tokenize()
    # print(f"{tokens}")

    pars = Parser(tokens)
    ast = pars.parse()
    # print(f'{ast}')

    inter = Interpreter(ast)
    result = inter.run()

    ptext = re.split("\n", text)

    for i, line in enumerate(ptext):
        print(f"{line.strip()} = {result[i]}")

except CustomError as e:
    # print the error without the traceback
    print(e, file=sys.stderr)
    print(errorText.makeErrorText(e.pos))

except Exception as e:
    print(e)
