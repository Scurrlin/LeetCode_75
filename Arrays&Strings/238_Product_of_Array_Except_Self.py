# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.

# You must write an algorithm that runs in O(n) time and without using the
# division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [1] * n
        s = [1] * n

        for i in range(1, n):
            p[i] = p[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            s[i] = s[i + 1] * nums[i + 1]
        
        answer = [p[i] * s[i] for i in range(n)]

        return answer