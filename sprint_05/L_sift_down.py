# L Просеивание вниз


def sift_down(heap, idx) -> int:
    heap_max_index = len(heap)-1
    left = idx * 2
    right = idx * 2 + 1

    # нет дочерних узлов
    if left > heap_max_index:
        return idx
    
        # проверяем, что есть оба дочерних узла
    if right <= heap_max_index and heap[right] > heap[left]:
        index_largest = right
    else:
        index_largest = left
    # отправляем максимум на вершину кучи и рекурсивно завпускаем просеивание в ребенке
    if heap[index_largest] > heap[idx]:
        heap[index_largest], heap[idx] = heap[idx], heap[index_largest]
        return sift_down(heap, index_largest)
    return idx
            
def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5

if __name__ == '__main__':
    test()