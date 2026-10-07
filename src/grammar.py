
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