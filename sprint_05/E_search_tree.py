# E Дерево поиска.
import os

from math import inf

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


# def append_vertices(vertices, node, min_value, max_value):
#     if min_value < node.value < max_value:
#         vertices.append((node.value, node)


def solution(root) -> bool:
    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        curr, min_val, max_val = stack.pop()
        
        # 1. Проверяем значение текущего узла
        if not (min_val < curr.value < max_val):
            return False
            
        # 2. Добавляем правого ребенка (если есть)
        # Для него: минимум обновляется на значение текущего узла
        if curr.right:
            stack.append((curr.right, curr.value, max_val))
            
        # 3. Добавляем левого ребенка (если есть)
        # Для него: максимум обновляется на значение текущего узла
        if curr.left:
            stack.append((curr.left, min_val, curr.value))

    return True
        
        
       


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

if __name__ == '__main__':
    test()