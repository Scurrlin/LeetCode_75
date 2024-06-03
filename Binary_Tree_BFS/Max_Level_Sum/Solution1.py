class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        
        while queue:
            level_sum = 0
            level_length = len(queue)
            
            for _ in range(level_length):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = len(queue) + 1
        
        return max_level