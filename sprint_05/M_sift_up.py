def sift_up(heap, idx) -> int:
    if idx == 1:
        return idx
    parent = idx // 2
    if heap[idx] > heap[parent]:
        heap[idx], heap[parent] = heap[parent], heap[idx]
        return sift_up(heap, parent)

    return idx # Если менять не нужно, возвращаем текущий индекс


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1

if __name__ == '__main__':
    test()