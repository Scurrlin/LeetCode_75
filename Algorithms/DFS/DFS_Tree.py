class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def dfs_tree(node, visited = None):
    if visited is None:
        visited = set()
    visited.add(node)
    result = [node.val]
    if node.left and node.left not in visited:
        result.extend(dfs_tree(node.left, visited))
    if node.right and node.right not in visited:
        result.extend(dfs_tree(node.right, visited))
    return result