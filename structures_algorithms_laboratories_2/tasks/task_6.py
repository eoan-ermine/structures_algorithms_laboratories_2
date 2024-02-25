import typer

from ..structures.deque import Deque


def split(integers):
    negatives = Deque()
    positives = Deque()

    for i in integers:
        if i < 0:
            negatives.push_back(i)
        else:
            positives.push_back(i)

    return (negatives, positives)


def pop_to_str(deque):
    res = []
    while len(deque) != 0:
        res.append(deque.front())
        deque.pop_front()
    return res


def main(filename: str):
    with open(filename, "r") as r:
        negatives, positives = split([int(e) for e in r.read().split()])
        print("Отрицательные:", " ".join([str(e) for e in pop_to_str(negatives)]))
        print("Положительные:", " ".join([str(e) for e in pop_to_str(positives)]))


def __start__():
    typer.run(main)