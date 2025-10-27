# Find all valid combinations of k numbers that sum up to n such that the
# following conditions are true:

# Only numbers 1 through 9 are used. Each number is used at most once. Return a
# list of all possible valid combinations. The list must not contain the same
# combination twice, and the combinations may be returned in any order.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(curr, n, i):
            if k == len(curr):
                if n == 0:
                    ans.append(curr.copy())
                return
            for digit in range(i, 10):
                curr.append(digit)
                backtrack(curr, n - digit, digit + 1)
                curr.pop()
        backtrack([], n, 1)
        return ans