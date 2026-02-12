# I Ограниченная очередь

class MyQueueSized:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def push(self, x):
        if len(self.queue) < self.max_size:
            self.queue.append(x)
        else:
            print("error")

    def pop(self):
        if self.queue:
            print(self.queue.pop(0))
        else:
            print("None")

    def peek(self):
        if self.queue:
            print(self.queue[0])
        else:
            print("None")

    def size(self):
        print(len(self.queue))

    
count = int(input())
queue = MyQueueSized(int(input()))

commands = {
    "push": lambda arg: queue.push(int(arg[0])),
    "pop": lambda _: queue.pop(),
    "peek": lambda _: queue.peek(),
    "size": lambda _: queue.size()
}

for _ in range(count):
    command, *arg = input().split()
    commands[command](arg)

