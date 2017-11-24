import sys

class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        for i in range(len(self.items)):
            sys.stdout.write(" ")
            sys.stdout.write(str(self.items[i]))
        print "\n"


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(34)
    queue.enqueue(44)
    queue.display()
