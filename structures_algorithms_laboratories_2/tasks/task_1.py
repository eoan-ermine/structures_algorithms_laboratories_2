import typer

from ..structures.deque import Deque


def decrypt(cypher: str):
    cypher_symbols = Deque(["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"])
    restore_deque = Deque()
    result = ""

    for symbol in cypher:
        while cypher_symbols.front() != symbol:
            restore_deque.push_back(cypher_symbols.front())
            cypher_symbols.pop_front()
        for i in range(2):
            restore_deque.push_back(cypher_symbols.front())
            cypher_symbols.pop_front()
        result += cypher_symbols.front()

        while len(restore_deque) != 0:
            cypher_symbols.push_front(restore_deque.back())
            restore_deque.pop_back()

    return result


def main(filename: str, output_filename: str):
    with open(filename, "r") as r:
        cypher = r.read()
        decypher = decrypt(cypher) 
        with open(output_filename, "w") as f:
            print(decypher)
            print(decypher, file=f)


def __start__():
    typer.run(main)