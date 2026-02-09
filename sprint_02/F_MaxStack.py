# F MaxStack

class StackMax:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.items:
            self.items.pop()
        else:
            print("error")
    
    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print("None")
    

stack = StackMax()

commands = {
        "push": lambda arg: stack.push(int(arg[0])),
        "pop": lambda _: stack.pop(),
        "get_max": lambda _: stack.get_max()
    }

for _ in range(int(input())):
    command, *arg = input().split()
    commands[command](arg)
