# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell, 1 representing a fresh orange, or 2 representing
# a rotten orange. Every minute, any fresh orange that is 4-directionally
# adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:      
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        fresh, rotten = 0, deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mins = 0

        while rotten and fresh > 0:
            rottenCount = len(rotten)
            for _ in range(rottenCount):
                rottenRow, rottenCol = rotten.popleft()

                for directionRow, directionCol in directions:
                    neighborRow = rottenRow + directionRow
                    neighborCol = rottenCol + directionCol

                    if (0 <= neighborRow < rows
                        and 0 <= neighborCol < cols
                        and grid[neighborRow][neighborCol] == 1):
                        grid[neighborRow][neighborCol] = 2
                        rotten.append((neighborRow, neighborCol))
                        fresh -= 1
            mins += 1

        return mins if fresh == 0 else -1