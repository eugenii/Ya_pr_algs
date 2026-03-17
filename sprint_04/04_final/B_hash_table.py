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
        # 3. Логика добавления:
        # - Находим нужную корзину через индекс
        # - Если ключ уже есть в списке корзины — ОБНОВЛЯЕМ значение
        # - Если ключа нет — ДОБАВЛЯЕМ пару [key, value] в список
        busket = self.table[self._get_hash_index(key)]
        if key in busket:
            busket[key] = value
        else:
            busket.append([key, value])
        
    def get(self, key):
        # 4. Логика поиска:
        # - Идем в нужную корзину
        # - Перебираем элементы списка. Нашли ключ — вернули value
        # - Не нашли — возвращаем None (или вызываем ошибку)
        busket = self.table[self._get_hash_index(key)]
        for k, v in busket:
            if k == key:
                return v
        return None
        
    def delete(self, key):
        # 5. Логика удаления:
        # - Идем в нужную корзину
        # - Находим индекс элемента в списке по ключу
        # - Удаляем (например, через pop() или del) и возвращаем значение
        busket = self.table[self._get_hash_index(key)]
        for i, (k, v) in enumerate(busket):
            if k == key:
                del busket[i]


count = int(input())

hash_table = HashTable()

# Словарь команд
commands = {
    "put": lambda arg: hash_table.put(int(arg[0]), int(arg[1])),
    "get": lambda arg: hash_table.get(int(arg[0])),
    "delete": lambda arg: hash_table.delete(int(arg[0])),
}
for _ in range(count):
    command, *arg = input().split()
    result = commands[command](arg)
    print(result)


        
