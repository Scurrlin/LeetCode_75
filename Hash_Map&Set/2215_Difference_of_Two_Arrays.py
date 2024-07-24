# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of
# size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in
# nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in
# nums1.
# Note that the integers in the lists may be returned in any order.

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        lst1 = [num for num in nums1_set if num not in nums2_set]
        lst2 = [num for num in nums2_set if num not in nums1_set]

        return [lst1, lst2]