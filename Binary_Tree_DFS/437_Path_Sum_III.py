# Given the root of a binary tree and an integer targetSum, return the number of
# paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node: TreeNode, currentSum: int, target: int, prefixSums: dict[int, int]) -> int:
            cSum, pSums = currentSum, prefixSums
            if not node:
                return 0
            
            cSum += node.val
            count = pSums.get(cSum - target, 0)
            pSums[cSum] = pSums.get(cSum, 0) + 1
            count += dfs(node.left, cSum, target, pSums)
            count += dfs(node.right, cSum, target, pSums)
            pSums[cSum] -= 1
            return count
        
        pSums = {0: 1}
        return dfs(root, 0, targetSum, pSums)