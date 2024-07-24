# Given an array of integers arr, return true if the number of occurrences of
# each value in the array is unique or false otherwise.

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        return len(count.values()) == len(set(count.values()))
