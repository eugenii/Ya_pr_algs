# B Комбинации.

keyboard = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

def combinations(number, index, current_res, final_list):
    # Базовый случай: дошли до конца строки цифр
    if index == len(number):
        final_list.append(current_res)
        return

    # Берем буквы, соответствующие текущей цифре
    letters = keyboard[number[index]]
    for letter in letters:
        # Рекурсивный переход к следующей цифре
        combinations(number, index + 1, current_res + letter, final_list)

digits = input().strip()

# Если ввод пустой, ничего не выводим
if digits:
    results = []
    combinations(digits, 0, "", results)
    print(" ".join(results))