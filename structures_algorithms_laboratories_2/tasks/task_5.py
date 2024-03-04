import typer

from ..structures.stack import Stack
from ..utils import print_list


def split(text):
    text = text[::-1]

    letters = Stack()
    digits = Stack()
    others = Stack()

    for c in text:
        if c.isalpha():
            letters.push(c)
        elif c.isdigit():
            digits.push(c)
        else:
            others.push(c)
    
    return (letters, digits, others)


def pop_to_str(stack):
    res = ""
    while len(stack) != 0:
        res += stack.pop()
    return res


def main(filename: str, output_filename: str):
    with open(filename, "r") as r:
        letters, digits, others = split(r.read())
        output_list = [f"Буквы: {pop_to_str(letters)}", f"Цифры: {pop_to_str(digits)}", f"Остальное: {pop_to_str(others)}"]
        print_list(output_list)
        with open(output_filename, "w") as f:
            print_list(output_list, file=f)


def __start__():
    typer.run(main)