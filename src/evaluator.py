from grammar import Expression, Statement



class Evaluator:

    def execute(self, statement):
        value = self.evaluate(statement.expression)

        if isinstance(statement, Statement.Print):
            print(self.stringify(value))

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