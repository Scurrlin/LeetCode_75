# Consider all the leaves of a binary tree, from left to right order, the values
# of those leaves form a leaf value sequence.

# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.

# Return true if and only if the two given trees with head nodes root1 and root2
# are leaf-similar.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def collect_leaf_values(root: TreeNode) -> str:
            if not root:
                return ''
            if not root.left and not root.right:
                return str(root.val)
            return collect_leaf_values(root.left) + collect_leaf_values(root.right)
        
        return collect_leaf_values(root1) == collect_leaf_values(root2)