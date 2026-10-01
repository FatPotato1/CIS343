#used an LLM to help with running tests since the directory is in a different spot
# --- start AI code ---
import sys
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO

# Go from test/lab1/test1.py to the CIS343 project folder.
ROOT = Path(__file__).resolve().parents[2]

# Allow Python to find scanner.py and tokens.py inside src.
sys.path.insert(0, str(ROOT / "src"))

from scanner import Scanner
from tokens import TokenType
# --- end AI code ---

class TestScanner(unittest.TestCase):
    def test_single_character_tokens(self):
        scanner = Scanner("()+;")
        tokens = scanner.scan()

        actual = [token.type for token in tokens]
        expected =[
            TokenType.LEFT_PAREN,
            TokenType.RIGHT_PAREN,
            TokenType.PLUS,
            TokenType.SEMICOLON,
            TokenType.EOF,
        ]

        self.assertEqual(actual, expected)

    def test_number(self):
        scanner = Scanner("12.5")
        tokens = scanner.scan()

        self.assertEqual(tokens[0].type, TokenType.NUMBER)
        self.assertEqual(tokens[0].lexeme, "12.5")
        self.assertEqual(tokens[0].literal, 12.5)
        self.assertFalse(scanner.had_error)

    def test_string(self):
        scanner = Scanner('"Hello there"')
        tokens = scanner.scan()

        self.assertEqual(tokens[0].type, TokenType.STRING)
        self.assertEqual(tokens[0].lexeme, '"Hello there"')
        self.assertEqual(tokens[0].literal, "Hello there")

    def test_keyword_and_identifier(self):
        scanner = Scanner("var variable")
        tokens = scanner.scan()

        self.assertEqual(tokens[0].type, TokenType.VAR)
        self.assertEqual(tokens[1].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[1].lexeme, "variable")

    def test_comment(self):
        scanner = Scanner("// This is a funny comment please dont scan\n+")
        tokens = scanner.scan()

        self.assertEqual(
            [token.type for token in tokens],
            [TokenType.PLUS, TokenType.EOF],
        )
        self.assertEqual(tokens[0].line, 2)

    #Used AI just for how to test for this test since I was having problems with it
    # --- start AI code ---
    def test_unexpected_character(self):
        scanner = Scanner("\n@")
        output = StringIO()

        # Capture the error printed by the scanner.
        with redirect_stdout(output):
            tokens = scanner.scan()

        self.assertTrue(scanner.had_error)
        self.assertIn("[line 2]", output.getvalue())
        self.assertIn("Unexpected character", output.getvalue())
        self.assertEqual(tokens[-1].type, TokenType.EOF)
        # --- end AI code ---

    def test_unterminated_string(self):
        scanner = Scanner('"you forgot the other quotes you fool')
        output = StringIO()

        with redirect_stdout(output):
            scanner.scan()

        self.assertTrue(scanner.had_error)
        self.assertIn("bad string", output.getvalue())

    def test_empty_input(self):
        scanner = Scanner("")
        tokens = scanner.scan()

        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, TokenType.EOF)
        self.assertFalse(scanner.had_error)


if __name__ == "__main__":
    unittest.main()
