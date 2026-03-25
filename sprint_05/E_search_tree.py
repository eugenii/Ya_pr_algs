# E Дерево поиска.
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def append_vertices(left_vertices, right_vertices, node):
    if node.left:
        left_vertices.append(node.left)
    if node.right:
        right_vertices.append(node.right)


def solution(root) -> bool:
    left_vertices, right_vertices = [], []
    left_value, right_value = root.value, root.value

    append_vertices(left_vertices, right_vertices, root)
    while left_vertices or right_vertices:
        if left_vertices:
            vertex = left_vertices.pop()
            if vertex.value > left_value:
                return False
            append_vertices(left_vertices, right_vertices, vertex)
            left_value = vertex.value
        if right_vertices:
            vertex = right_vertices.pop()
            if vertex.value < right_value:
                return False
            append_vertices(left_vertices, right_vertices, vertex)
            right_value = vertex.value
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