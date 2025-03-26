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
parser.add_argument(
    "--show", action="store_true", help=" shows the generated tokens and AST (optional)"
)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    "-cl", "--cline", help="uses command-line argument as input expressions"
)
group.add_argument(
    "-f", "--filepath", type=extention_validation, help="uses file as input (*.mat)"
)
args = parser.parse_args()

try:
    if args.cline:
        text = args.cline
    elif args.filepath:
        with open(args.filepath, "r") as file:
            text = file.read()
            print(text)

    errorText = ErrorText(text)
    lex = Lexer(text)
    tokens = lex.tokenize()

    pars = Parser(tokens)
    ast = pars.parse()

    if args.show:
        print(f"-------------\nTokens:\n{tokens}")
        print(f"-------------\nAbstract Syntax Tree:\n{ast}\n")

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
        print("Output:")
        print("".join(s[:-1]))

except CustomError as e:
    print(e)
    print(errorText.makeErrorText(e.pos))

except Exception as e:
    print(e)
