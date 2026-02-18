# B Калькулятор (польская нотация).
# Ссылка на успешное решение: https://contest.yandex.ru/contest/22781/run-report/157097940/
# Для реализации используется стек.
# Команды калькулятора записаны в словарь, при вызове передаются аргументы в lambda-функцию
# Операнды забираются  с вершины стека.
# При  достижении конца строки выводится результат. Как показала ошибка в тренажёре - необходим последний элемент.
# При вычислении сначала берётся второй операнд, затем первый.

stack = []

data = input().split()

commands = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: int(x / y),
}

for i in range(len(data)):
    if data[i] in commands:
        y = stack.pop()
        x = stack.pop()
        stack.append(commands[data[i]](x, y))
    else:
        stack.append(int(data[i]))
print(stack[0])
