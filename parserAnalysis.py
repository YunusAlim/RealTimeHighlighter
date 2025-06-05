from lexicalAnalysis import TokenType

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def lookahead(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def match(self, expected_type, expected_value=None):
        token = self.lookahead()
        if token and token.type == expected_type and (expected_value is None or token.value == expected_value):
            self.pos += 1
            return True
        return False

    def parse(self):
        while self.pos < len(self.tokens):

            if self.lookahead().type == TokenType.COMMENT:
                self.pos += 1
                continue
            if not self.stmt():
                return False
        return True

    def stmt(self):
        while self.lookahead() and self.lookahead().type == TokenType.COMMENT:
            self.pos += 1  # yorum satırlarını atla

        token = self.lookahead()
        if token is None:
            return False

        if token.type == TokenType.TYPE:
            return self.decl_stmt()
        elif token.type == TokenType.ID:
            return self.assign_stmt()
        elif token.type == TokenType.KEYWORD and token.value == "if":
            return self.if_stmt()
        elif token.type == TokenType.KEYWORD and token.value == "while":
            return self.while_stmt()
        return False

    def decl_stmt(self):
        if self.match(TokenType.TYPE):
            if self.match(TokenType.ID):
                if self.match(TokenType.OP, "="):
                    if self.expr():
                        return self.match(TokenType.SEMICOLON)
        return False

    def assign_stmt(self):
        if self.match(TokenType.ID):
            if self.match(TokenType.OP, "="):
                if self.expr():
                    return self.match(TokenType.SEMICOLON)
        return False

    def if_stmt(self):
        if self.match(TokenType.KEYWORD, "if"):
            if self.match(TokenType.PAREN, "("):
                if self.condition():
                    if self.match(TokenType.PAREN, ")"):
                        return self.block()
        return False

    def while_stmt(self):
        if self.match(TokenType.KEYWORD, "while"):
            if self.match(TokenType.PAREN, "("):
                if self.condition():
                    if self.match(TokenType.PAREN, ")"):
                        return self.block()
        return False

    def condition(self):
        if not self.expr():
            return False
        if not self.match(TokenType.COMPARISON):
            return False
        return self.expr()

    def block(self):
        if not self.match(TokenType.BRACE, "{"):
            return False
        while self.lookahead() and self.lookahead().type != TokenType.BRACE:
            if self.lookahead().type == TokenType.COMMENT:
                self.pos += 1
                continue
            if not self.stmt():
                return False
        return self.match(TokenType.BRACE, "}")

    def expr(self):
        if not self.term():
            return False
        while self.lookahead() and self.lookahead().type == TokenType.OP and self.lookahead().value in ('+', '-'):
            self.pos += 1
            if not self.term():
                return False
        return True

    def term(self):
        token = self.lookahead()
        if token and token.type in (TokenType.NUMBER, TokenType.ID):
            self.pos += 1
            return True
        return False
