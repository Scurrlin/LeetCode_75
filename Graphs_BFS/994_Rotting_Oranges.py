# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell, 1 representing a fresh orange, or 2 representing
# a rotten orange. Every minute, any fresh orange that is 4-directionally
# adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:      
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        fresh_cnt = 0
        rotten = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        
        minutes_passed = 0
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue                        
                    fresh_cnt -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))

        return minutes_passed if fresh_cnt == 0 else -1