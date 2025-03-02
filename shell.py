import lexer



# while True:
# text = input("> ")
text = "2+3*5/(1+1)\n3+5"
lex = lexer.Lexer(text)

try:
    tokens = lex.tokenize()
    print(f"{tokens}")
except Exception as e:
    print(f"{e}")
    # break

