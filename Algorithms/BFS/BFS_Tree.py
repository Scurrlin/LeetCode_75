from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def bfs_tree(root):
    if not root:
        return []
    visited = set()
    deq = deque([root])
    result = []
    while deq:
        node = deq.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node.val)
            if node.left:
                deq.append(node.left)
            if node.right:
                deq.append(node.right)
    return result