# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may
# rotate these shapes.

# Given an integer n, return the number of ways to tile an 2 x n board. Since
# the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different
# if and only if there are two 4-directionally adjacent cells on the board such
# that exactly one of the tilings has both squares occupied by a tile.

class Solution(object):
    def numTilings(self, n):
        dp = [1, 2, 5] + [0] * n
        for i in range(3, n):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % 1000000007
        return dp[n - 1]