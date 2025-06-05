from lexicalAnalysis import tokenize
from parserAnalysis import Parser

def main():
    input_code = "int x = 5 + y;"
    print("Input Code:", input_code)

    tokens = tokenize(input_code)
    print("Tokens:")
    for token in tokens:
        print(token)

    parser = Parser(tokens)
    if parser.parse():
        print("✔ Syntax is valid.")
    else:
        print("❌ Syntax error detected.")

if __name__ == "__main__":
    main()
