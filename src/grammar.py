
class Expression:

    class Literal:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f"{self.value}"


    class Unary:
        def __init__(self, operator, operand):
            self.operator = operator
            self.operand = operand

        def __str__(self):
            return f"({self.operator.lexeme} {self.operand})"

    class Binary:
        def __init__(self, left_operand, operator, right_operand):
            self.left_operand = left_operand
            self.operator = operator
            self.right_operand = right_operand

        def __str__(self):
            return f"({self.operator.lexeme} " f"{self.left_operand} {self.right_operand})"

    class Group:
        def __init__(self, expression):
            self.expression = expression

        def __str__(self):
            return f"(group {self.expression})"

    class Variable:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name.lexeme

    class Assign:
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __str__(self):
            return f"(= {self.name.lexeme} {self.value})"

class Statement:
    class Expression:
        def __init__(self, expression):
            self.expression = expression

    class Print:
        def __init__(self, expression):
            self.expression = expression

    class Var:
        def __init__(self, name, initializer):
            self.name = name
            self.initializer = initializer

    class Block:
        def __init__(self, statements):
            self.statements = statements