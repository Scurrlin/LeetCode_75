# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the
# resulting array. Return 0 if there is no such subarray.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prevWindow = currWindow = max_length = 0

        for num in nums:
            if num == 0:
                max_length = max(max_length, prevWindow + currWindow)
                prevWindow, currWindow = currWindow, 0
            else:
                currWindow += 1

        max_length = max(max_length, prevWindow + currWindow)
        return max_length if currWindow < len(nums) else currWindow - 1