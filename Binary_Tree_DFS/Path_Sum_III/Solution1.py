class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node: TreeNode, current_sum: int, target: int, prefix_sums: dict[int, int]) -> int:
            if not node:
                return 0
            current_sum += node.val
            count = prefix_sums.get(current_sum - target, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            count += dfs(node.left, current_sum, target, prefix_sums)
            count += dfs(node.right, current_sum, target, prefix_sums)
            prefix_sums[current_sum] -= 1
            return count
        
        prefix_sums = {0: 1}
        return dfs(root, 0, targetSum, prefix_sums)