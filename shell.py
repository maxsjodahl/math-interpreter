import lexer

while True:
    text = input("> ")
    lex = lexer.Lexer(text)
    
    try:
         lex.tokenize()
    except Exception as e:
        print(f"{e}")
        break
    
    print(f"{lex.tokens}")