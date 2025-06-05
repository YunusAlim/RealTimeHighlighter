from enum import Enum

class TokenType(Enum):
    TYPE = "TYPE"
    ID = "ID"
    NUMBER = "NUMBER"
    OP = "OP"
    SEMICOLON = "SEMICOLON"
    BRACE = "BRACE"
    PAREN = "PAREN"
    COMPARISON = "COMPARISON"
    KEYWORD = "KEYWORD"
    COMMENT = "COMMENT"
    WHITESPACE = "WHITESPACE"
    UNKNOWN = "UNKNOWN"

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"[{self.type.name}: {self.value}]"

def tokenize(text):
    tokens = []
    i = 0
    types = {"int", "float"}
    keywords = {"if", "while"}
    comparisons = {"<", ">", "==", "!=", "<=", ">="}

    while i < len(text):
        c = text[i]

        if c.isspace():
            i += 1
            continue


        if text[i:i+2] == "//":
            start = i
            i += 2
            while i < len(text) and text[i] != '\n':
                i += 1
            tokens.append(Token(TokenType.COMMENT, text[start:i]))
            continue

        # Multi-char
        if text[i:i+2] in comparisons:
            tokens.append(Token(TokenType.COMPARISON, text[i:i+2]))
            i += 2
            continue

        if c in comparisons:
            tokens.append(Token(TokenType.COMPARISON, c))
            i += 1
            continue

        if c.isalpha():
            start = i
            while i < len(text) and (text[i].isalnum() or text[i] == '_'):
                i += 1
            word = text[start:i]
            if word in types:
                tokens.append(Token(TokenType.TYPE, word))
            elif word in keywords:
                tokens.append(Token(TokenType.KEYWORD, word))
            else:
                tokens.append(Token(TokenType.ID, word))


        elif c.isdigit():

            start = i

            has_dot = False

            while i < len(text) and (text[i].isdigit() or (text[i] == '.' and not has_dot)):

                if text[i] == '.':
                    has_dot = True

                i += 1

            tokens.append(Token(TokenType.NUMBER, text[start:i]))


        elif c in {'+', '-', '='}:
            tokens.append(Token(TokenType.OP, c))
            i += 1

        elif c == ';':
            tokens.append(Token(TokenType.SEMICOLON, c))
            i += 1

        elif c in {'{', '}'}:
            tokens.append(Token(TokenType.BRACE, c))
            i += 1

        elif c in {'(', ')'}:
            tokens.append(Token(TokenType.PAREN, c))
            i += 1

        else:
            tokens.append(Token(TokenType.UNKNOWN, c))
            i += 1

    return tokens
