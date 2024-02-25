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


def main(filename: str):
    with open(filename, "r") as r:
        res = check_parens(r.read())
        if res:
            print("Скобочки в порядке")
        else:
            print("Скобочки не в порядке")


def __start__():
    typer.run(main)