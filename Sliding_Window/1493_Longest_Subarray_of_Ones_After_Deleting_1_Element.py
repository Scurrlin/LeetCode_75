# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the
# resulting array. Return 0 if there is no such subarray.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zero, count = 0, 0, 1
        for right in range(len(nums)) :
            if nums[right] == 0 :
                count -= 1
                zero = 1
            if count < 0 :
                if nums[left] == 0 :
                    count += 1
                left += 1
        return right - left