# A Поисковая системма.
from collections import defaultdict


def get_rel_words(words: dict, query: set) -> int:
    """
    Подсчет релевантности слов в запросе.
    arguments:
        words - словарь слов и их частотой
        query - запрос
    returns:
        result - релевантность запроса.
    """
    result = 0
    for word in query:
        if word in words:
            result += words[word]
    return result

# Получаем данные.
n = int(input())
data = []
for i in range(n):
    item = defaultdict(int)
    for word in input().split():
        item[word] += 1
    data.append(dict(item))

print('data - >', data)

# Получаем запросы.
m = int(input())
queries = [set(input().split()) for _ in range(m)]
print('queries - >', queries)

result_relevants = [[] for _ in range(n)]
print( result_relevants)
# Для каждого запроса...
for q in range(len(queries)):
    # ...подсчитываем релевантность слов по каждому документу.
    relevants = {}
    for doc in range(len(data)):
        relevants[doc + 1] = get_rel_words(data[doc], queries[q])
    print('relevants - >', relevants)
    result_relevants[q] = list(relevants.values())
    relevants.clear()

print(result_relevants)



