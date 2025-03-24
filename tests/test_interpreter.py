import pytest

from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter
from src.util import CustomError, ErrorText

def _setup_interpreter(expression):
    lex = Lexer(expression)
    tokens = lex.tokenize()

    pars = Parser(tokens)
    ast = pars.parse()

    inter = Interpreter(ast)
    result = inter.run()
    return result



def test_valid_expression():
    
    result = _setup_interpreter("3*(5+15/(1+2*2))-1")
    assert result[0] == 23, "expected 23 but got {}".format(result)

    result = _setup_interpreter("3*(5+15/(1+2*2))--1")
    assert result[0] == 25, "expected 25 but got {}".format(result)

    result = _setup_interpreter("3*(5+15/(1+2*2))+-1")
    assert result[0] == 23, "expected 23 but got {}".format(result)

def test_invalid_syntax():

    with pytest.raises(CustomError) as excinfo:
        _setup_interpreter("3**(5+15/(1+2*2))-1")

    assert "factor error: unexpected value" in str(excinfo.value)

    with pytest.raises(CustomError) as excinfo:
        _setup_interpreter("3(5+15/(1+2*2))-1")

    assert "syntax error: expected operand" in str(excinfo.value)

    with pytest.raises(CustomError) as excinfo:
            _setup_interpreter("3*(5+15/(1+2*2))1")

    assert "syntax error: expected operand, got '1'" in str(excinfo.value)

    with pytest.raises(CustomError) as excinfo:
            _setup_interpreter("1---1")

    assert "syntax error: unexpected factor" in str(excinfo.value)

def test_invalid_expression():
     
    with pytest.raises(CustomError) as excinfo:
        _setup_interpreter("")

    assert "factor error: unexpected value" in str(excinfo.value)

    with pytest.raises(CustomError) as excinfo:
        _setup_interpreter("13 13")

    assert "syntax error: expected operand" in str(excinfo.value)