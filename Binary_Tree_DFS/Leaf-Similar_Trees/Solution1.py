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