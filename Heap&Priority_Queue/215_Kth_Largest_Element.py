# Given an integer array nums and an integer k, return the kth largest element
# in the array.

# Note that it is the kth largest element in the sorted order, not the kth
# distinct element.

# Can you solve it without sorting?

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]

# Sorting solution

class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k-1]