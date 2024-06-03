class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(curr, n, i):
            if k == len(curr):
                if n == 0:
                    ans.append(curr.copy())
                return
            for dig in range(i, 10):
                curr.append(dig)
                backtrack(curr, n - dig, dig + 1)
                curr.pop()
        backtrack([], n, 1)
        return ans

# curr = current