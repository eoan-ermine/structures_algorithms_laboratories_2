class Stack:
    def __init__(self, arr = []):
        self.__items = []
        for e in arr:
            self.push(e)

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()
    
    def back(self):
        return self.__items[-1]
    
    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)