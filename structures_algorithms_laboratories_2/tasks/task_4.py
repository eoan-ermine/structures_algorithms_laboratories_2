import typer

from ..structures.deque import Deque

def check_brackets(text):
    s = Deque()
    for c in text:
        if c == "[":
            s.push_back(c)
        elif c == "]":
            if len(s) == 0:
                return False
            s.pop_back()
    return len(s) == 0


def main(filename: str, output_filename: str):
    with open(filename, "r") as r:
        res = check_brackets(r.read())
        output = "Квадоатные скобочки в порядке" if res else "Квадоатные скобочки не в порядке"
        print(output)
        with open(output_filename, "w") as f:
            print(output, file=f)


def __start__():
    typer.run(main)