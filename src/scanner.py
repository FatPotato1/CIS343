from tokens import Token, TokenType

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.had_error = False

    def scan(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(
            Token(TokenType.EOF, "", None, self.line)
        )
        return self.tokens

    def scan_token(self):
        character = self.advance()

        single_character_tokens ={
            "(": TokenType.LEFT_PAREN,
            ")": TokenType.RIGHT_PAREN,
            "{": TokenType.LEFT_BRACE,
            "}": TokenType.RIGHT_BRACE,
            ",": TokenType.COMMA,
            ".": TokenType.DOT,
            "-": TokenType.MINUS,
            "+": TokenType.PLUS,
            ";": TokenType.SEMICOLON,
            "/": TokenType.SLASH,
            "*": TokenType.STAR,
        }

        if character in single_character_tokens:
            self.add_token(single_character_tokens[character])

        else:
            self.had_error = True

            #used AI here to give the exact line and characters causing errors
            # --- start AI code ---
            print(f"[line {self.line}] Error: "
                f"Unexpected character: {character!r}"
            )
            # --- end AI code ---


    def advance(self):
        character = self.source[self.current]
        self.current += 1
        return character

    def add_token(self, token_type, literal=None):
        lexeme = self.source[self.start:self.current]
        self.tokens.append(
            Token(token_type, lexeme, literal, self.line)
        )

    def is_at_end(self):
        return self.current >= len(self.source)