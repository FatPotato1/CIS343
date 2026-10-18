import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from scanner import Scanner
from parser import Parser


class testParser(unittest.TestCase):
    def test_number(self):
        output = "5.0"
        tokens = Scanner("5").scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

    def test_string(self):
        output = "coolstring"
        tokens = Scanner('"coolstring"').scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

#used ai for this
    # --- start AI code ---
    def test_boolean_and_nil(self):
        for source, output in (("true", "True"),("false", "False"),("nil", "None"),):
            with self.subTest(source=source):
                tokens = Scanner(source).scan()
                input = Parser(tokens).parse()
                self.assertEqual(str(input), output)
    # ---end AI code ---
    def test_unary(self):
        output = "(- 5.0)"
        tokens = Scanner("-5").scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

    def test_nested_unary(self):
        output = "(! (! (- 5.0)))"
        tokens = Scanner("!!-5").scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

    def test_binary(self):
        output = "(+ 2.0 3.0)"
        tokens = Scanner("2 + 3").scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

    def test_group(self):
        output = "(group 5.0)"
        tokens = Scanner("(5)").scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

    def test_precedence(self):
        output = "(+ 2.0 (* 3.0 4.0))"
        tokens = Scanner("2 + 3 * 4").scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

#used AI to figure out what other tests I needed, but i wrote these all entirely myself
    def test_group_changes_precedence(self):
        output = "(* (group (+ 2.0 3.0)) 4.0)"
        tokens = Scanner("(2 + 3) * 4").scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

    def test_comparison_and_equality(self):
        output = "(== (< 1.0 2.0) True)"
        tokens = Scanner("1 < 2 == true").scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

    def test_left_associative(self):
        output = "(- (- 10.0 3.0) 2.0)"
        tokens = Scanner("10 - 3 - 2").scan()
        input = Parser(tokens).parse()
        self.assertEqual(str(input), output)

    def test_missing_operand(self):
        tokens = Scanner("1 +").scan()
        with self.assertRaises(SyntaxError):
            Parser(tokens).parse()

if __name__ == "__main__":
    unittest.main()