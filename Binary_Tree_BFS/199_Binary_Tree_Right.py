# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to bottom.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        v = []
        def dfs(node, level):
            if node:
                if level == len(v):
                    v.append(node.val)
                dfs(node.right, level + 1)
                dfs(node.left, level + 1)
                
        dfs(root, 0)
        return v

# v = view