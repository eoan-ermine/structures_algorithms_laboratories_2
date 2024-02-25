import typer

from ..structures.stack import Stack


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


def main(filename: str):
    with open(filename, "r") as r:
        letters, digits, others = split(r.read())
        print("Буквы: ", pop_to_str(letters))
        print("Цифры: ", pop_to_str(digits))
        print("Остальное: ", pop_to_str(others))


def __start__():
    typer.run(main)