class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while (res := guess(mid := ((high + low) >> 1))) != 0:
            if res == -1: high = mid - 1
            else: low = mid + 1
        return mid