# J Спиочная очередь

class LinkedQueue:
    def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

    def get(self):
        """Вывести элемент, находящийся в голове очереди, и удалить его.
        Если очередь пуста, то вывести «error»"""
        ...

    def put(self, value):
        """Добавить элемент в очередь"""
        ...

    def size(self):
        """Вывести количество элементов в очереди"""
        ...