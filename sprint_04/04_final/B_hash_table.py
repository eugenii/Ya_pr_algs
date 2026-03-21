# B Хеш таблица.
# ссылка на успешное решение: https://contest.yandex.ru/contest/24414/run-report/158743396/
# Задача Б реализует хеш-таблицу с разрешением коллизий методом цепочек, 
# обеспечивая среднюю сложность O(1)для операций вставки, получения и удаления 
# при O(N) по памяти в худшем случае (если все ключи попали в одну корзину).


class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next  # Ссылка на следующий узел


class HashTable:
    def __init__(self, size=100003):
        self.size = size
        # Создаем массив из None. 
        # Теперь каждая ячейка — это потенциальная "голова" списка.
        self.table = [None] * self.size

    def _get_hash_index(self, key):
        # 2. Вычисляем индекс корзины
        # Используем остаток от деления на размер таблицы
        return abs(hash(key)) % self.size

    def put(self, key, value):
        index = self._get_hash_index(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            return
        
        # Если в корзине уже кто-то есть, идем по цепочке
        current = self.table[index]
        while True:
            if current.key == key:
                current.value = value # Обновляем, если ключ совпал
                return
            if current.next is None:
                break
            current = current.next
    
        # Если дошли до конца и не нашли совпадений — добавляем в хвост
        current.next = Node(key, value)
        

    def get(self, key):
        index = self._get_hash_index(key)
        # Начинаем с самого первого узла в корзине
        current = self.table[index]
        
        # Идем по цепочке, пока не упремся в None (конец цепи)
        while current is not None:
            if current.key == key:
                return current.value  # Нашли нужный ключ — вернули значение
            current = current.next    # Переходим к следующему "звену"
            
        # Если прошли всю цепь и не нашли ключ
        return "None"

    def delete(self, key):
        index = self._get_hash_index(key)
        current = self.table[index]
        previous = None

        while current is not None:
            if current.key == key:
                result = current.value
                
                if previous is None:
                    # Случай А: Удаляем самый первый узел
                    self.table[index] = current.next
                else:
                    # Случай Б: "Перебрасываем" ссылку через текущий узел
                    previous.next = current.next
                
                return result
                
            # Двигаем указатели вперед по цепи
            previous = current
            current = current.next

        return "None"



count = int(input())

ht = HashTable()

# Словарь команд
commands = {
    "put": lambda arg: ht.put(int(arg[0]), int(arg[1])),
    "get": lambda arg: ht.get(int(arg[0])),
    "get": lambda arg: ht.get(int(arg[0])),
    "delete": lambda arg: ht.delete(int(arg[0])),
}
# Читаем количество команд n
for _ in range(count):
    command = input().split()
    cmd_name = command[0]
    
    if cmd_name == 'put':
        ht.put(int(command[1]), int(command[2]))
    elif cmd_name == 'get':
        print(ht.get(int(command[1])))
    elif cmd_name == 'delete':
        print(ht.delete(int(command[1])))
