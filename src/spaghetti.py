import sys
from scanner import Scanner
from parser import Parser

class Spaghetti:
    def repl(self):
        print("REPL mode")
        while True:
            try:
                source = input("> ")
                self.run(source)

            except (KeyboardInterrupt, EOFError):
                break

    def run_file(self, filename):
        with open(filename, "r") as file:
            source = file.read()

        self.run(source)

    def run(self, source):
        scanner = Scanner(source)
        tokens = scanner.scan()

        if scanner.had_error:
            return
        try:
            tree = Parser(tokens).parse()
            print(tree)
        except SyntaxError as error:
            print(error)

if __name__ == "__main__":
    spaghetti = Spaghetti()
    if len(sys.argv) == 1:
        spaghetti.repl()
    elif len(sys.argv) == 2:
        spaghetti.run_file(sys.argv[1])
    else:
        print("Too many files, try: spaghetti.py [filename].spaghetti")




