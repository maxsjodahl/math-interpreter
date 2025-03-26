import src.lexer as lexer
import src.parser as parser
from src.util import CustomError


##### INTERPRETER #####


class Interpreter:
    def __init__(self, ast):
        self.ast = ast

    def run(self):
        result = []
        for expr in self.ast:
            result.append(self.interpret(expr))
        return result

    def interpret(self, astNode):
        if isinstance(astNode, parser.NumberNode):
            return astNode.token.value

        elif isinstance(astNode, parser.UnaryNode):
            if astNode.s_token.type in [lexer.T_MINUS]:
                return 0 - astNode.v_token.value
            elif astNode.s_token.type in [lexer.T_PLUS]:
                return astNode.v_token.value

        elif isinstance(astNode, parser.BinaryNode):
            match astNode.op.type:
                case lexer.T_MUL:
                    return self.interpret(astNode.left) * self.interpret(astNode.right)

                case lexer.T_DIV:
                    right = self.interpret(astNode.right)
                    if right != 0:
                        return self.interpret(astNode.left) / right
                    else:
                        raise CustomError(
                            "error: cannot divide with 0", astNode.op.position
                        )

                case lexer.T_PLUS:
                    return self.interpret(astNode.left) + self.interpret(astNode.right)

                case lexer.T_MINUS:
                    return self.interpret(astNode.left) - self.interpret(astNode.right)

                case _:
                    raise CustomError(
                        f"error: unexpected binary operation {astNode.op.type}",
                        astNode.op.position,
                    )
