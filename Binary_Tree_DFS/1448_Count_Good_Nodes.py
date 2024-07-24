# Given a binary tree root, a node X in the tree is named good if in the path
# from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)