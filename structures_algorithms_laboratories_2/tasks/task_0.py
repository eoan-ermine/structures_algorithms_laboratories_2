import typer

from ..structures.deque import Deque


def merge_sort(arr):
    def merge(left, right):
        result = Deque()

        while len(left) != 0 and len(right) != 0:
            if left.front() < right.front():
                result.push_back(left.front())
                left.pop_front()
            else:
                result.push_back(right.front())
                right.pop_front()
        
        while len(left) != 0:
            result.push_back(left.front())
            left.pop_front()
        while len(right) != 0:
            result.push_back(right.front())
            right.pop_front()

        return result
 
    if len(arr) <= 1:
        return Deque(arr)
    
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    return merge(
        merge_sort(left_half),
        merge_sort(right_half)
    )

def main(filename: str, output_filename: str):
    with open(filename, "r") as r:
        lines = merge_sort([e.strip() for e in r.readlines()])
        with open(output_filename, "w") as f:
            while len(lines) != 0:
                print(lines.front())
                print(lines.front(), file=f)
                lines.pop_front()

def __start__():
    typer.run(main)