# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left). If the
# current direction is right, move to the right child of the current node;
# otherwise, move to the left child. Change the direction from right to left or
# from left to right. Repeat the second and third steps until you can't move in
# the tree. Zigzag length is defined as the number of nodes visited - 1. (A
# single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0

        def dfs(node, left, right):
            self.maximum = max(self.maximum, left, right)
            
            if node.left:
                dfs(node.left, right + 1, 0)
            if node.right:
                dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.maximum