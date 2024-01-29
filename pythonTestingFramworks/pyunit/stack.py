class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return None

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


