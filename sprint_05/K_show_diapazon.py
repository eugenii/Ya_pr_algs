# K-means clustering
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def print_range(node, l, r):
    if not node:
        return

    # 1. Проверяем, есть ли смысл идти ВЛЕВО
    # Если значение текущего узла >= L, то слева могут быть числа из диапазона
    # (так как там могут быть и равные узлы, идем даже если равно L)
    if node.value >= l:
        print_range(node.left, l, r)

    # 2. Проверяем сам узел
    if l <= node.value <= r:
        print(node.value, end=' ')

    # 3. Проверяем, есть ли смысл идти ВПРАВО
    # Если значение узла <= R, то справа могут быть подходящие числа
    if node.value <= r:
        print_range(node.right, l, r)




def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test()
