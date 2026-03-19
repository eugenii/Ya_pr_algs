# A поисковая система
#   ссылка на успешное решение: https://contest.yandex.ru/contest/24414/run-report/158670893/
# Решение задачи А использует инвертированный индекс для создания карты слов к документам, 
# обеспечивая временную сложность поиска O(M + K log K), где K - количество документов. 
#  через накопление релевантности, при этом построение индекса занимает O(L) времени и памяти.

from collections import defaultdict

index = defaultdict(lambda: defaultdict(int))
for i in range(int(input())):
    for word in input().split():
        index[word][i] += 1

for _ in range(int(input())):
    # Для каждого запроса:
    relevance = defaultdict(int)
    query_words = set(input().split())  # Берем только УНИКАЛЬНЫЕ слова из запроса

    for word in query_words:
        if word in index:
            # Прямо здесь бежим по всем документам, где есть это слово
            for doc_id, count in index[word].items():
                relevance[doc_id] += count

    # Сейчас в relevance есть только те документы, где релевантность > 0
    # Сортируем: сначала по убыванию баллов (-x[1]), потом по возрастанию ID (x[0])
    sorted_docs = sorted(relevance.items(), key=lambda x: (-x[1], x[0]))

    # Забираем первые 5 ID (не забываем +1, так как в индексе они с нуля)
    result = [doc_id + 1 for doc_id, count in sorted_docs[:5]]
    print(*result)