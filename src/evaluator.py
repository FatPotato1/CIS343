from grammar import Expression


class Evaluator:
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