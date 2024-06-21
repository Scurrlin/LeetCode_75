class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_tree(node, v=None):
    if v is None:
        v = set()
    v.add(node)
    result = [node.val]
    if node.left and node.left not in v:
        result.extend(dfs_tree(node.left, v))
    if node.right and node.right not in v:
        result.extend(dfs_tree(node.right, v))
    return result