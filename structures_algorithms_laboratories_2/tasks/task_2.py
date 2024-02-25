import typer

from ..structures.stack import Stack


def solve_hanoi(source_tower, dest_tower, temp_tower, logger = None):
    def move_is_legal(from_tower, to_tower):
        if len(from_tower) == 0:
            return False
        if len(to_tower) == 0:
            return True
        return from_tower.back() < to_tower.back()

    def move_from_to(source_tower, dest_tower):
        if move_is_legal(source_tower, dest_tower):
            dest_tower.push(source_tower.pop())
        else:
            source_tower.push(dest_tower.pop())

    n = len(source_tower)
    i = 0
    moves = [(source_tower, temp_tower), (source_tower, dest_tower), (temp_tower, dest_tower)] \
            if n % 2 == 0 else \
            [(source_tower, dest_tower), (source_tower, temp_tower), (temp_tower, dest_tower)]

    while len(dest_tower) != n:
        move_from_to(moves[i % 3][0], moves[i % 3][1])
        if logger:
            print(source_tower, dest_tower, file=logger)
        i += 1


def main(filename: str = "hanoi_setup.txt", output_filename: str = "hanoi_result.txt", log_filename: str = "log.txt"):
    with open(filename, "r") as r:
        n = int(r.read().strip())

        source_tower = Stack([n - i for i in range(n)])
        dest_tower = Stack()
        temp_tower = Stack()

        with open(log_filename, "w") as log:
            solve_hanoi(source_tower, dest_tower, temp_tower, log)

        with open(output_filename, "w") as f:
            print("n: ", n, file=f)
            print("Source tower:", source_tower, file=f)
            print("Destination tower:", dest_tower, file=f)
            print("Temp tower:", temp_tower, file=f)


def __start__():
    typer.run(main)