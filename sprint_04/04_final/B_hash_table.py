# B Хеш таблица.


class HashTable:
    def __init__(self, size=100003):
        # 1. Создаем массив "корзин" (buckets)
        # Каждая корзина — это вначале пустой список []
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _get_hash_index(self, key):
        # 2. Вычисляем индекс корзины
        # Используем остаток от деления на размер таблицы
        return abs(hash(key)) % self.size

    def put(self, key, value):
        index = self._get_hash_index(key)
        # Ищем ключ в корзине
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Обновляем значение
                return
        # Если не нашли — добавляем новую пару
        self.table[index].append([key, value])
        
    def get(self, key):
        index = self._get_hash_index(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return "None"
        
    def delete(self, key):
        index = self._get_hash_index(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                # Удаляем и возвращаем ЗНАЧЕНИЕ
                result = bucket[i][1]
                bucket.pop(i)
                return result
        return "None" # Важно возвращать строку "None" для вывода



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


        
