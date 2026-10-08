
grammar and design choices:

I followed lox and the slides pretty much exactly, and did the lox/lisp implementation with the literals, unary, binary and group implementations. 
<br>
<br>

grammar:

<br>
expression: literal | unary | binary | grouping

literal: NUMBER | STRING | "true" | "false" | 

unary: ("-" |"!") expression

binary: expression operator expression

grouping    "(" expression ")"

operator: "+" | "-" | "*" | "/"
           | "==" | "!=" | "<" | "<=" | ">" | ">="

<br>

<br>

setup: for printer tests, just run test2.py in lab2 folder. All code for lab 2 is in test2 and grammar.py

test cases:

(the actual output and expected output are all the same, since all unittests passed, also meaning that all results match expectations)




Test_literal, unary, binary, and group

- purpose: self explanatory, test these grammar types to make sure expected printed result matches

        code:
        
        
        literal:
        
        
                output = "coolstring"
                input = Expression.Literal("coolstring")
        
        unary:
        
                output = "(- 5)"
                input = Expression.Unary( Token(TokenType.MINUS, "-", None, 1), Expression.Literal(5))
                self.assertEqual(output, str(input))
        
        binary:
        
        
                output = "(+ 2 3)"
                input = Expression.Binary(
                    Expression.Literal(2),
                    Token(TokenType.PLUS, "+", None, 1),
                    Expression.Literal(3),
                )
                self.assertEqual(str(input), output)
        
        group:
        
                output = "(group 5)"
                input = Expression.Group(Expression.Literal(5))
                self.assertEqual(str(input), output)

- test_powerpoint_case

purpose: used the testcase listed in your slides to make sure output matched. I think that I could have different ways of representing because it is my own langauge? However, for this part i am just sticking with the standard lox/lisp way listed in the slides

    code:

    input = Expression.Binary(
            Expression.Unary(Token(TokenType.MINUS, "-", None, 1), Expression.Literal(123)),
            Token(TokenType.STAR, "*", None, 1),
            Expression.Group(Expression.Literal(45.67)))
        output = "(* (- 123) (group 45.67))"

        self.assertEqual(str(input), output)

- test_stupidly_long_gpt_case

purpose: a big testcase that i prompted chatgpt to make, and to try to include many different edge cases and categories that I couldn't think of.

    code:

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