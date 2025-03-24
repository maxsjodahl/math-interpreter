import argparse
import re
from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter
from src.util import CustomError, ErrorText


def extention_validation(filepath):
    if not filepath.endswith(".mat"):
        raise argparse.ArgumentTypeError("filepath must end with '.mat'")
    return filepath


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="specified output file (optional)")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    "-cl", "--cline", help="uses command-line argument as input expressions"
)
group.add_argument(
    "-f", "--filepath", type=extention_validation, help="uses file as input (*.mat)"
)
args = parser.parse_args()
# while True:
try:
    # text = input("> ")
    if args.cline:
        text = args.cline
    elif args.filepath:
        with open(args.filepath, "r") as file:
            text = file.read()
            print(text)

    errorText = ErrorText(text)
    # text = "2+3*5"
    lex = Lexer(text)
    tokens = lex.tokenize()
    # print(f"{tokens}")

    pars = Parser(tokens)
    ast = pars.parse()
    # print(f'{ast}')

    inter = Interpreter(ast)
    result = inter.run()

    ptext = re.split("\n|;", text)

    s = []
    for i, line in enumerate(ptext):
        st = line.strip()
        if st == "":
            s.append("\n")
            continue

        s.append(f"{st} = {result[i]}")
        s.append("\n")

    if args.output:
        f = open(args.output, "x")
        f.write("".join(s[:-1]))
    else:
        print("\nOutput:")
        print("".join(s[:-1]))

except CustomError as e:
    # print the error without the traceback
    print(e)
    print(errorText.makeErrorText(e.pos))
    # print(e.pos)

except Exception as e:
    print(e)
    # traceback.print_exc()
