# Consider all the leaves of a binary tree, from left to right order, the values
# of those leaves form a leaf value sequence.

# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.

# Return true if and only if the two given trees with head nodes root1 and root2
# are leaf-similar.

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def collect_leaf_values(root: TreeNode, leaf_values: list[int]) -> None:
            if not root:
                return
            if not root.left and not root.right:
                leaf_values.append(root.val)

            collect_leaf_values(root.left, leaf_values)
            collect_leaf_values(root.right, leaf_values)
        
        leaf_values1, leaf_values2 = [], []
        collect_leaf_values(root1, leaf_values1)
        collect_leaf_values(root2, leaf_values2)
        
        return leaf_values1 == leaf_values2