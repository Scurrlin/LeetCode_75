# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k
# and remove them from the array.

# Return the maximum number of operations you can perform on the array.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, ops = 0, len(nums) - 1, 0

        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                ops += 1
                l += 1
                r -= 1
            elif total < k:
                l += 1
            else:
                r -= 1
        return ops