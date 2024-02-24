import enum

class Deque:
    class Direction(enum.Enum):
        LEFT = 1
        RIGHT = 2

    def __init__(self):
        self.__CHUNK_SIZE = 8
        self.__chunks = []
        self.__size = 0
        self.__left_idx = 0
        self.__start_chunk = 0

        self.__allocate(Deque.Direction.RIGHT)

    def __need_allocation(self, direction):
        if direction == Deque.Direction.LEFT:
            return self.__left_idx == 0
        else:
            return len(self.__chunks[-1]) == self.__CHUNK_SIZE

    def __allocate(self, direction):
        if direction == Deque.Direction.LEFT:
            self.__chunks.insert(0, [])
        else:
            self.__chunks.append([])

    def __get_chunk(self, idx):
        return (self.__left_idx + idx) // self.__CHUNK_SIZE
    
    def __get_idx(self, idx):
        def impl(idx, reverse):
            idx = (self.__left_idx + idx) % self.__CHUNK_SIZE
            if reverse:
                return self.__CHUNK_SIZE - idx - 1
            else:
                return idx

        return impl(idx, self.__get_chunk(idx) < self.__start_chunk)

    def push_front(self, value):
        if self.__need_allocation(Deque.Direction.LEFT):
            self.__allocate(Deque.Direction.LEFT)
            self.__start_chunk += 1
        if self.__left_idx == 0:
            self.__left_idx = self.__CHUNK_SIZE - 1
        else:
            self.__left_idx = self.__left_idx - 1
        self.__chunks[0].append(value)
        self.__size += 1
    
    def pop_front(self, value):
        self.__chunks[0].pop()
        self.__size -= 1

    def push_back(self, value):
        if self.__need_allocation(Deque.Direction.RIGHT):
            self.__allocate(Deque.Direction.RIGHT)
        self.__chunks[-1].append(value)
        self.__size += 1

    def pop_back(self, value):
        self.__chunks[-1].pop()
        self.__size -= 1

    def front(self):
        return self.__chunks[0][-1]
    
    def back(self):
        return self.__chunks[-1][-1]

    def __getitem__(self, idx):
        return self.__chunks[self.__get_chunk(idx)][self.__get_idx(idx)]

    def __len__(self):
        return self.__size