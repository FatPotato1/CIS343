import sys

def repl():
    print("REPL mode")
    while True:
        try:
            input("> ")
            print("Scanner Not Implemented")

        except KeyboardInterrupt:
            break

def run_file(filename):
    with open(filename, "r") as file:
        source = file.read()

    print("Scanner Not Implemented")



if len(sys.argv) == 1:
    repl()
elif len(sys.argv) == 2:
    run_file(sys.argv[1])
else:
    print("Too many files, try: lox.py [filename].lox")




