import typer

from ..structures.stack import Stack


def reverse_lines(lines):
    stack = Stack(lines)
    res = []
    while len(stack) != 0:
        res.append(stack.pop())
    return res


def main(filename: str, output_filename: str):
    with open(filename, "r") as r:
        lines = reverse_lines([e.strip() for e in r.readlines()])
        with open(output_filename, "w") as f:
            for e in lines:
                print(e, file=f)

def __start__():
    typer.run(main)