# Финальная задача спринта 8 "Шпаргалка"
# Yandex Contest successful solution ID https://contest.yandex.ru/contest/26133/run-report/162591986/      (162591986)
# Асимптотика алгоритма
# 1. Временная сложность (Time Complexity): O(W * L_w + |T| * L_max)
# - O(W * L_w)\) — время на построение Бора, где W — количество слов в словаре, 
# а L_w — их средняя длина (мы просто один раз проходим по всем буквам всех слов)
# O(|T| *L_max) — время работы основного цикла, где |T| — длина текста, а L_max — длина самого длинного слова в 
# словаре. В худшем случае из каждой позиции текста мы можем пройти по Бору вглубь не более чем на 
# длину самого длинного слова [1]. В цифрах задачи это максимум 100000 * 100 = 10^7 операций, что легко 
# укладывается в 1 секунду.
# 2. Пространственная сложность (Space Complexity): O(W * L_w + |T|)
# O(W * L_w) — память, которую занимает Бор. В худшем случае под каждую букву каждого слова создается узел дерева 
# (если буквы не пересекаются).
# O(|T|) — память под массив dp длиной |T| + 1.

import sys


def build_trie(words):
    trie = {}
    for word in words:
        current_node = trie
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node["is_terminal"] = True
    return trie


data = sys.stdin.read().splitlines()

T = data[0]
count = int(data[1])
words = [word for word in data[2:]]
trie = build_trie(words)

dp = [False] * (len(T) + 1)
dp[0] = True

for i in range(len(T)):
    if dp[i]:
        current_node = trie
        j = i

        while j < len(T) and T[j] in current_node:
            current_node = current_node[T[j]]
            j += 1

            if current_node.get("is_terminal"):
                dp[j] = True

if dp[-1]:
    print("YES")
else:
    print("NO")