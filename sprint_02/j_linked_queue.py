# J Спиочная очередь

class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


class LinkedQueue:
    def __init__(self, value=None, next_item=None):
        self.length = 0
        self.head = None
        self.tail = None

    def get(self):
        """Вывести элемент, находящийся в голове очереди, и удалить его.
        Если очередь пуста, то вывести «error»"""
        if self.length == 0:
            return 'error'
        else:
            value = self.head.value
            self.head = self.head.next_item
            self.length -= 1
            if self.length == 0:
                self.tail = None
        return value

    def put(self, value):
        """Добавить элемент в очередь"""
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next_item = Node(value)
            self.tail = self.tail.next_item
        self.length += 1

    def size(self):
        """Вывести количество элементов в очереди"""
        return self.length


queue = LinkedQueue()

commands = {
        'get': lambda _: print(queue.get()),
        'put': lambda arg: queue.put(int(arg[0])),
        'size': lambda _: print(queue.size())
}


for _ in range(int(input())):
    command, *arg = input().split()
    commands[command](arg)
