# A Дек

class Deque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, item):
        if self.size == self.max_size:
            return "error"
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size  # не понял - для чего %?
        self.size += 1

    def push_front(self, item):
        if self.size == self.max_size:
            return "error"
        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = item
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            return "error"
        self.tail = (self.tail - 1) % self.max_size
        x = self.items[self.tail]
        self.size -= 1
        print(x)

    def pop_front(self):
        if self.size == 0:
            return "error"
        x = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        print(x)


count, n = int(input()), int(input())

dequeue = Deque(n)

commands = {
    "push_front": lambda arg: dequeue.push_front(int(arg[0])),
    "push_back": lambda arg: dequeue.push_back(int(arg[0])),
    "pop_front": lambda _: dequeue.pop_front(),
    "pop_back": lambda _: dequeue.pop_back(),
}

for _ in range(count):
    command, *arg = input().split()
    result = commands[command](arg)
    if result is not None: 
        print(result)

