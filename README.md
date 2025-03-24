# Math Interpreter

## Introduction
The Math Interpreter is a Python-based application designed to evaluate mathematical expressions from the command line or a file. It supports basic arithmetic operations and can handle expressions with parentheses and floating-point numbers.

## Features
- Supports mathematical expressions including addition, subtraction, multiplication, and division.
- Handles parentheses for grouped operations.
- Supports both command-line input and file input.
- Custom error handling with informative messages.
- Optional output file to save results.

## Installation
Make sure you have Python 3 installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage
Run the interpreter from the command line as follows:

```bash
python3 main.py --help
```

This will display the following help message:

```
usage: main.py [-h] [-o OUTPUT] (-cl CLINE | -f FILEPATH)

options:
  -h, --help            show this help message and exit
  -o, --output OUTPUT   specified output file (optional)
  -cl, --cline CLINE    uses command-line argument as input expressions
  -f, --filepath FILEPATH
                        uses file as input (*.mat)
```

### Examples
#### Using Command-Line Input
```bash
python3 main.py -cl "3*(5+15/(1+2*2))-1"
```

#### Using a File as Input
```bash
python3 main.py -f expressions.mat
```

#### Specifying an Output File
```bash
python3 main.py -cl "5+3*2" -o result.txt
```

## Running Tests
To run the test suite, use:
```bash
pytest tests/ -v
```

## Project Structure
```
math-interpreter/
├── src/
│   ├── lexer.py
│   ├── parser.py
│   ├── interpreter.py
│   └── __init__.py
├── tests/
│   ├── test_interpreter.py
│   └── __init__.py
├── main.py
├── requirements.txt
└── README.md
```

## License
This project is licensed under the MIT License.


