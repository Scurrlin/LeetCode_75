from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs_tree(root):
    if not root:
        return []
    v = set()
    q = deque([root])
    result = []
    while q:
        node = q.popleft()
        if node not in v:
            v.add(node)
            result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result