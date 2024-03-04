import typer

from ..structures.stack import Stack

def check_parens(text):
    s = Stack()
    for c in text:
        if c == "(":
            s.push(c)
        elif c == ")":
            if len(s) == 0:
                return False
            s.pop()
    return len(s) == 0


def main(filename: str, output_filename: str):
    with open(filename, "r") as r:
        res = check_parens(r.read())
        output = "Скобочки в порядке" if res else "Скобочки не в порядке"
        print(output)
        with open(output_filename, "w") as f:
            print(output, file=f)


def __start__():
    typer.run(main)