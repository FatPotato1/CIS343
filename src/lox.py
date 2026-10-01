import sys
from scanner import Scanner

class Lox:
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

        for token in tokens:
            token.print_token()

if __name__ == "__main__":
    lox = Lox()
    if len(sys.argv) == 1:
        lox.repl()
    elif len(sys.argv) == 2:
        lox.run_file(sys.argv[1])
    else:
        print("Too many files, try: lox.py [filename].lox")




