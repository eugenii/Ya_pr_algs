from typing import Optional
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def remove(root, key) -> Optional[Node]:
    if not root:
        return None
    
    # Узел есть, проверяем "лево-право" рекурсивно и в конце концов удалим
    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    # Попали на удаляемый узел
    else:  
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # Случай 3: Есть оба ребенка
        # 1. Находим минимальный узел в правом поддереве
        successor = root.right
        while successor.left is not None:
            successor = successor.left
        
        # 2. Подменяем значение текущего узла значением преемника
        root.value = successor.value
        
        # 3. Удаляем преемника из правого поддерева
        root.right = remove(root.right, successor.value)
    
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8


if __name__ == '__main__':
    test()