from grammar import Expression, Statement
from environment import Environment


class Evaluator:

    #used ai on a few parts of this
    # --- start AI code ---
    def __init__(self):
        self.environment = Environment()

    def execute(self, statement):
        if isinstance(statement, Statement.Var):
            value = None
            if statement.initializer is not None:
                value = self.evaluate(statement.initializer)

            self.environment.define(statement.name.lexeme, value)
            return

        if isinstance(statement, Statement.Block):
            self.execute_block(statement.statements, Environment(self.environment))
            return

        if isinstance(statement, Statement.Print):
            value = self.evaluate(statement.expression)
            print(self.stringify(value))
            return

        if isinstance(statement, Statement.Expression):
            self.evaluate(statement.expression)
    # --- end AI code ---

    def execute_block(self, statements, environment):
        previous = self.environment

        try:
            self.environment = environment

            for statement in statements:
                self.execute(statement)

        finally:
            self.environment = previous

    # used AI on some of this part
    # --- start AI code ---
    def stringify(self, value):
        if value is None:
            return "nil"
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)

    # --- end AI code ---

    def evaluate(self, node):

        if isinstance(node, Expression.Variable):
            return self.environment.get(node.name)

        if isinstance(node, Expression.Assign):
            value = self.evaluate(node.value)
            return self.environment.assign(node.name, value)

        if isinstance(node, Expression.Literal):
            return node.value

        if isinstance(node, Expression.Group):
            return self.evaluate(node.expression)

        if isinstance(node, Expression.Unary):
            value = self.evaluate(node.operand)

            if node.operator.lexeme == "-":
                return -value
            if node.operator.lexeme == "!":
                return not value

        if isinstance(node, Expression.Binary):
            left = self.evaluate(node.left_operand)
            right = self.evaluate(node.right_operand)
            operator = node.operator.lexeme

            if operator == "+":
                return left + right
            if operator == "-":
                return left - right
            if operator == "*":
                return left * right
            if operator == "/":
                return left / right
            if operator == "==":
                return left == right
            if operator == "!=":
                return left != right
            if operator == ">":
                return left > right
            if operator == ">=":
                return left >= right
            if operator == "<":
                return left < right
            if operator == "<=":
                return left <= right