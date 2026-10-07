import sys
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from grammar import Expression
from tokens import Token, TokenType

class testGrammar(unittest.TestCase):
    def test_literal(self):
        output = "coolstring"
        input = Expression.Literal("coolstring")
        self.assertEqual(output, str(input))

    def test_Unary(self):
        output = "(- 5)"
        input = Expression.Unary( Token(TokenType.MINUS, "-", None, 1), Expression.Literal(5))
        self.assertEqual(output, str(input))

    def test_Binary(self):
        output = "(+ 2 3)"
        input = Expression.Binary(
            Expression.Literal(2),
            Token(TokenType.PLUS, "+", None, 1),
            Expression.Literal(3),
        )
        self.assertEqual(str(input), output)

    def test_group(self):
        output = "(group 5)"
        input = Expression.Group(Expression.Literal(5))
        self.assertEqual(str(input), output)

    def test_powerpoint_case(self):

        input = Expression.Binary(
            Expression.Unary(Token(TokenType.MINUS, "-", None, 1), Expression.Literal(123)),
            Token(TokenType.STAR, "*", None, 1),
            Expression.Group(Expression.Literal(45.67)))
        output = "(* (- 123) (group 45.67))"

        self.assertEqual(str(input), output)

#threw in one chatgpt case that is obnoxiously long for fun and maybe find edge cases I didn't think about

    def test_stupidly_long_gpt_case(self):
        # --- start AI code ---
        # One deliberately long case to check varied, nested AST structures.
        output = (
            "(== "
            "(group (!= "
            "(group (< (group (+ (- 123) "
            "(* 4.5 (group (- 10 (/ 9 3)))))) (- (- 0)))) "
            "(! (group (>= "
            "(group (/ (+ 100 20) (group (* 2 3)))) "
            "(group (- 25 5))))))) "
            "(group (== "
            "(group (<= (group (+ 0 0.125)) (group (group 0.125)))) "
            "(group (!= "
            "(group (> (- (- 8)) 7)) "
            "(group (== (+ pasta sauce) pastasauce)))))))"
        )

        input = Expression.Binary(
            Expression.Group(
                Expression.Binary(
                    Expression.Group(
                        Expression.Binary(
                            Expression.Group(
                                Expression.Binary(
                                    Expression.Unary(
                                        Token(TokenType.MINUS, "-", None, 1),
                                        Expression.Literal(123),
                                    ),
                                    Token(TokenType.PLUS, "+", None, 1),
                                    Expression.Binary(
                                        Expression.Literal(4.5),
                                        Token(TokenType.STAR, "*", None, 1),
                                        Expression.Group(
                                            Expression.Binary(
                                                Expression.Literal(10),
                                                Token(TokenType.MINUS, "-", None, 1),
                                                Expression.Binary(
                                                    Expression.Literal(9),
                                                    Token(TokenType.SLASH, "/", None, 1),
                                                    Expression.Literal(3),
                                                ),
                                            )
                                        ),
                                    ),
                                )
                            ),
                            Token(TokenType.LESS, "<", None, 1),
                            Expression.Unary(
                                Token(TokenType.MINUS, "-", None, 1),
                                Expression.Unary(
                                    Token(TokenType.MINUS, "-", None, 1),
                                    Expression.Literal(0),
                                ),
                            ),
                        )
                    ),
                    Token(TokenType.BANG_EQUAL, "!=", None, 1),
                    Expression.Unary(
                        Token(TokenType.BANG, "!", None, 1),
                        Expression.Group(
                            Expression.Binary(
                                Expression.Group(
                                    Expression.Binary(
                                        Expression.Binary(
                                            Expression.Literal(100),
                                            Token(TokenType.PLUS, "+", None, 1),
                                            Expression.Literal(20),
                                        ),
                                        Token(TokenType.SLASH, "/", None, 1),
                                        Expression.Group(
                                            Expression.Binary(
                                                Expression.Literal(2),
                                                Token(TokenType.STAR, "*", None, 1),
                                                Expression.Literal(3),
                                            )
                                        ),
                                    )
                                ),
                                Token(TokenType.GREATER_EQUAL, ">=", None, 1),
                                Expression.Group(
                                    Expression.Binary(
                                        Expression.Literal(25),
                                        Token(TokenType.MINUS, "-", None, 1),
                                        Expression.Literal(5),
                                    )
                                ),
                            )
                        ),
                    ),
                )
            ),
            Token(TokenType.EQUAL_EQUAL, "==", None, 1),
            Expression.Group(
                Expression.Binary(
                    Expression.Group(
                        Expression.Binary(
                            Expression.Group(
                                Expression.Binary(
                                    Expression.Literal(0),
                                    Token(TokenType.PLUS, "+", None, 1),
                                    Expression.Literal(0.125),
                                )
                            ),
                            Token(TokenType.LESS_EQUAL, "<=", None, 1),
                            Expression.Group(
                                Expression.Group(Expression.Literal(0.125))
                            ),
                        )
                    ),
                    Token(TokenType.EQUAL_EQUAL, "==", None, 1),
                    Expression.Group(
                        Expression.Binary(
                            Expression.Group(
                                Expression.Binary(
                                    Expression.Unary(
                                        Token(TokenType.MINUS, "-", None, 1),
                                        Expression.Unary(
                                            Token(TokenType.MINUS, "-", None, 1),
                                            Expression.Literal(8),
                                        ),
                                    ),
                                    Token(TokenType.GREATER, ">", None, 1),
                                    Expression.Literal(7),
                                )
                            ),
                            Token(TokenType.BANG_EQUAL, "!=", None, 1),
                            Expression.Group(
                                Expression.Binary(
                                    Expression.Binary(
                                        Expression.Literal("pasta"),
                                        Token(TokenType.PLUS, "+", None, 1),
                                        Expression.Literal("sauce"),
                                    ),
                                    Token(TokenType.EQUAL_EQUAL, "==", None, 1),
                                    Expression.Literal("pastasauce"),
                                )
                            ),
                        )
                    ),
                )
            ),
        )

        self.assertEqual(str(input), output)
    # --- end AI code ---