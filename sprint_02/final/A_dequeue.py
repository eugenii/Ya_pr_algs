# A Дек
# Решение основано на теории, описанной в тренажере.
# методы класса Deque вызываются в цикле, который считывает команды
# и их аргументы.
# Аргументы передаются в виде списка в словаре commands.
# Использование остатка от деления в операцих push_front и push_back позволяет
# реализовать циклическую очередь.
# ссылка на успешное решение: https://contest.yandex.ru/contest/22781/run-report/157058379/
# Асимптотическая сложность:
# По времени: 
# O(1) на одну операцию (команду push_front, push_back, pop_front, pop_back).
# Обоснование: Каждая операция с деком включает в себя лишь проверку 
# граничных условий (заполненность/пустота), арифметические операции с 
# индексами (взятие остатка от деления для кольцевого буфера) и вставку/чтение 
# элемента по индексу. В этих операциях нет циклов или рекурсии, которые 
# зависели бы от количества элементов в деке. Следовательно, время выполнения 
# каждой команды константно.

# По памяти: O(n)
# Обоснование: Мы выделяем массив фиксированного размера n (параметр max_size). 
# Дополнительной памяти, зависящей от количества элементов, не требуется. 
# Объем используемой памяти линейно зависит от максимально допустимого размера  дека.

class Deque:
    """
    Класс реализует дек с ограниченной длиной.
    """
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, item):
        """
        Добавляет item в конец дека. Error, если дек заполнен.
        """
        if self.size == self.max_size:
            return "error"
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, item):
        """
        Добавляет item в начало дека. Error, если дек заполнен.
        """
        if self.size == self.max_size:
            return "error"
        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = item
        self.size += 1

    def pop_back(self):
        """
        Удаляет и возвращает последний элемент дека. Error, если дек пуст.
        """
        if self.size == 0:
            return "error"
        self.tail = (self.tail - 1) % self.max_size
        x = self.items[self.tail]
        self.size -= 1
        print(x)

    def pop_front(self):
        """
        Удаляет и возвращает первый элемент дека. Error, если дек пуст.
        """
        if self.size == 0:
            return "error"
        x = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        print(x)


count, n = int(input()), int(input())

dequeue = Deque(n)

# Словарь команд
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

