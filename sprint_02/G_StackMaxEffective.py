# G StackMaxEffective

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(item)
        if not self.max_items or item >= self.max_items[-1]:
            self.max_items.append(item)

    def pop(self):
        if not self.items:
            print("error")
        else:
            item = self.items.pop()
            if item == self.max_items[-1]:
                self.max_items.pop()
            
    def get_max(self):
        if not self.max_items:
            print("None")
        else:
            print(self.max_items[-1])
    
    def top(self):
        if not self.items:
            print("error")
        else:
            print(self.items[-1])


stack = StackMaxEffective()

commands = {
    "push": lambda arg: stack.push(int(arg[0])),
    "pop": lambda _: stack.pop(),
    "get_max": lambda _: stack.get_max(),
    "top": lambda _: stack.top()
}

for _ in range(int(input())):
    command, *arg = input().split()
    commands[command](arg)
