
#used AI to figure out best way to implement this runtime error
# --- start AI code ---
class SpaghettiRuntimeError(RuntimeError):
    def __init__(self, token, message):
        super().__init__(f"[line {token.line}] {message}")

# --- end AI code ---
class Environment:
    def __init__(self, enclosing=None):
        self.values = {}
        self.enclosing = enclosing

    def define(self, name, value):
        self.values[name] = value

    def get(self, name):
        if name.lexeme in self.values:
            return self.values[name.lexeme]

        if self.enclosing is not None:
            return self.enclosing.get(name)

        raise SpaghettiRuntimeError(
            name, f"Undefined variable '{name.lexeme}'."
        )

    def assign(self, name, value):
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
            return value

        if self.enclosing is not None:
            return self.enclosing.assign(name, value)

        raise SpaghettiRuntimeError(
            name, f"Undefined variable '{name.lexeme}'."
        )
