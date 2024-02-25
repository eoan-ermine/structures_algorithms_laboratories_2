class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class Deque:    
    def __init__(self, arr=[]):
        self.head = None
        self.tail = None
        self.size = 0

        for e in arr:
            self.push_back(e)

    def push_front(self, item):
        new_node = Node(item)

        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
        
        self.head = new_node
        self.size += 1

    def push_back(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        
        self.tail = new_node
        self.size += 1
    
    def pop_front(self):
        old_first = self.head
        self.head = self.head.next
        self.size -= 1

        if self.head == None:
            self.tail = None
        else:
            self.head.prev = None
        
        return old_first.value

    def pop_back(self):
        old_last = self.tail
        self.size -= 1
        self.tail = old_last.prev

        if self.tail == None:
            self.head = None
        else:
            self.tail.next = None

        return old_last.value
    
    def front(self):
        return self.head.value
    
    def back(self):
        return self.tail.value

    def __len__(self):
        return self.size