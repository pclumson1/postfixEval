class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return self.items == []

    def is_full(self):
        return len(self.items) == self.capacity

    def push(self, item):
        if self.is_full():
            raise IndexError()
        else:
            self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError()
        else:
            temp = self.items[-1]
            self.items = self.items[0:-1]
            return temp

    def peek(self):
        if self.is_empty():
            raise IndexError()
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)
