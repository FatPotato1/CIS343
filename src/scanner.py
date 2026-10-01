from tokens import Token, TokenType

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.start_line = 1
        self.had_error = False
        self.single_character_tokens = {
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

        self.keywords = {
            "and": TokenType.AND,
            "class": TokenType.CLASS,
            "else": TokenType.ELSE,
            "false": TokenType.FALSE,
            "fun": TokenType.FUN,
            "for": TokenType.FOR,
            "if": TokenType.IF,
            "nil": TokenType.NIL,
            "or": TokenType.OR,
            "print": TokenType.PRINT,
            "return": TokenType.RETURN,
            "super": TokenType.SUPER,
            "this": TokenType.THIS,
            "true": TokenType.TRUE,
            "var": TokenType.VAR,
            "while": TokenType.WHILE,
        }

    def scan(self):
        while not self.end():
            self.start = self.current
            self.start_line = self.line
            self.scan_token()

        self.tokens.append(
            Token(TokenType.EOF, "", None, self.line)
        )
        return self.tokens

    def scan_token(self):
        character = self.next()

        if character in self.single_character_tokens:
            self.add_token(self.single_character_tokens[character])

        elif character == "!":
            if self.match("="):
                self.add_token(TokenType.BANG_EQUAL)
            else:
                self.add_token(TokenType.BANG)

        elif character == "=":
            if self.match("="):
                self.add_token(TokenType.EQUAL_EQUAL)
            else:
                self.add_token(TokenType.EQUAL)

        elif character == "<":
            if self.match("="):
                self.add_token(TokenType.LESS_EQUAL)
            else:
                self.add_token(TokenType.LESS)

        elif character == ">":
            if self.match("="):
                self.add_token(TokenType.GREATER_EQUAL)
            else:
                self.add_token(TokenType.GREATER)

        elif character == "/":
            if self.match("/"):
                # skip anything that is a comment
                while not self.end() and self.check_next() != "\n":
                    self.next()
            else:
                self.add_token(TokenType.SLASH)

        elif character in (" ", "\r", "\t"):
            pass

        elif character == "\n":
            self.line += 1

        elif character == '"':
            self.string()

        elif self.is_digit(character):
            self.number()

        elif self.is_alpha(character):
            self.identifier()


        else:
            self.had_error = True

            #used AI here to give the exact line and characters causing errors
            # --- start AI code ---
            print(f"[line {self.line}] Error: "
                f"Unexpected character: {character!r}"
            )
            # --- end AI code ---

    def string(self):
        while not self.end() and self.check_next() != '"':
            if self.check_next() == "\n":
                self.line += 1

            self.next()

        if self.end():
            print(self.start_line, "bad string")
            return

        # go past end quote
        self.next()

        # get rid of the quotes around the string
        value = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, value)


    def number(self):
        #go through remaining digits
        while self.is_digit(self.check_next()):
            self.next()

        #add a decimal point if a digit follows it
        if self.check_next() == "." and self.is_digit(self.check_next_next()):
            self.next()

            while self.is_digit(self.check_next()):
                self.next()

        value = float(self.source[self.start:self.current])
        self.add_token(TokenType.NUMBER, value)

    #a thing that has letters underscores and numbers
    def identifier(self):
        while self.is_alpha(self.check_next()) or self.is_digit(self.check_next()):
            self.next()

        text = self.source[self.start:self.current]
        if text in self.keywords:
            self.add_token(self.keywords[text])
        else:
            self.add_token(TokenType.IDENTIFIER)


#move to next character
    def next(self):

        character = self.source[self.current]
        self.current += 1
        return character

    #only go through next character if it matches
    def match(self, expected):
        if self.end():
            return False

        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    #check the next character without doing anything to it
    def check_next(self):
        if self.end():
            return ""

        return self.source[self.current]

    #same thing as above but with an extra character ahead
    def check_next_next(self):
        if self.current + 1 >= len(self.source):
            return ""

        return self.source[self.current + 1]


    #Used an LLM here to figure out how to check for these categories
    # --- start AI code ---
    def is_digit(self, character):
        return "0" <= character <= "9"


    def is_alpha(self, character):
        return (
                "a"<= character <="z"
                or "A" <= character <= "Z"
                or character == "_"
        )
    # --- end AI code ---

    def add_token(self, token_type, literal=None):
        lexeme = self.source[self.start:self.current]
        self.tokens.append(
            Token(token_type, lexeme, literal, self.start_line)
        )

    def end(self):
        return self.current >= len(self.source)