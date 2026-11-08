from grammar import Expression, Statement
from tokens import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    #reusing some of the functions like this one from the breakfast parser in-class assignment
    def peek(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None

    def expect(self, token_type):
        token = self.peek()
        if token is None:
            raise SyntaxError(
                f"Expected {token_type.name}, got end of input"
            )

        if token.type != token_type:
            raise SyntaxError(
                f"[line {token.line}] Expected {token_type.name}, "
                f"got {token.type.name} ({token.lexeme!r})"
            )

        self.current += 1
        return token

    def parse(self):
        tree = self.expression()

        token = self.peek()
        if token is not None and token.type != TokenType.EOF:
            raise SyntaxError(
                f"[line {token.line}] Unexpected token {token.lexeme!r}"
            )

        return tree

    def parse_program(self):
        statements = []
        errors = []

        while self.peek().type != TokenType.EOF:
            try:
                statements.append(self.statement())
            except SyntaxError as error:
                errors.append(error)
                self.synchronize()

        return statements, errors

    def statement(self):
        if self.peek().type == TokenType.PRINT:
            self.expect(TokenType.PRINT)
            expression = self.expression()
            self.expect(TokenType.SEMICOLON)
            return Statement.Print(expression)

        expression = self.expression()
        self.expect(TokenType.SEMICOLON)
        return Statement.Expression(expression)

    def synchronize(self):
        while self.peek().type != TokenType.EOF:
            token_type = self.peek().type

            if token_type == TokenType.PRINT:
                return

            self.expect(token_type)

            if token_type == TokenType.SEMICOLON:
                return

    def expression(self):
        return self.equality()

    def equality(self):
        # != and ==
        tree = self.comparison()
        while self.peek().type in (TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.expect(self.peek().type)
            right = self.comparison()
            tree = Expression.Binary(tree, operator, right)
        return tree

    def comparison(self):
        # >, >=, <, and <=
        tree = self.term()
        while self.peek().type in (TokenType.GREATER, TokenType.GREATER_EQUAL,TokenType.LESS, TokenType.LESS_EQUAL,):
            operator = self.expect(self.peek().type)
            right = self.term()
            tree = Expression.Binary(tree, operator, right)
        return tree

    def term(self):
        # - and +
        tree = self.factor()
        while self.peek().type in (TokenType.MINUS, TokenType.PLUS):
            operator = self.expect(self.peek().type)
            right = self.factor()
            tree = Expression.Binary(tree, operator, right)
        return tree

    def factor(self):
        # / and *
        tree = self.unary()
        while self.peek().type in (TokenType.SLASH, TokenType.STAR):
            operator = self.expect(self.peek().type)
            right = self.unary()
            tree = Expression.Binary(tree, operator, right)
        return tree

    def unary(self):
        # ! and -
        if self.peek().type in (TokenType.BANG, TokenType.MINUS):
            operator = self.expect(self.peek().type)
            return Expression.Unary(operator, self.unary())
        return self.primary()

    def primary(self):
    # number, string, true, false, or nil

    #used AI on a few parts of this
    # --- start AI code ---
        token = self.peek()
        if token.type in (TokenType.NUMBER, TokenType.STRING):
            self.expect(token.type)
            return Expression.Literal(token.literal)
        if token.type == TokenType.TRUE:
            self.expect(TokenType.TRUE)
            return Expression.Literal(True)
        if token.type == TokenType.FALSE:
            self.expect(TokenType.FALSE)
            return Expression.Literal(False)
        if token.type == TokenType.NIL:
            self.expect(TokenType.NIL)
            return Expression.Literal(None)
        if token.type == TokenType.LEFT_PAREN:
            self.expect(TokenType.LEFT_PAREN)
            tree = self.expression()
            self.expect(TokenType.RIGHT_PAREN)
            return Expression.Group(tree)

        raise SyntaxError(
            f"[line {token.line}] Expected a literal or '(', " f"got {token.type.name} ({token.lexeme!r})")
    # --- end AI code --