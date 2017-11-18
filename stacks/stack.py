class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        """ Remove and Return the last item inserted in the stack"""
        item = self.items.pop()
        return item

    def peek(self):
        """ Return the last item """
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def display(self):
        for i in reversed(range(len(self.items))):
            print self.items[i]


if __name__ == "__main__":
    stack = Stack()
    stack.push(20)
    stack.push(14)
    stack.display()
