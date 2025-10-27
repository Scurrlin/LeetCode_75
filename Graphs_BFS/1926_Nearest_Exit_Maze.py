# You are given an m x n matrix maze (0-indexed) with empty cells (represented
# as '.') and walls (represented as '+'). You are also given the entrance of the
# maze, where entrance = [entrancerow, entrancecol] denotes the row and column
# of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step
# into a cell with a wall, and you cannot step outside the maze. Your goal is to
# find the nearest exit from the entrance. An exit is defined as an empty cell
# that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the
# nearest exit, or -1 if no such path exists.

from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        deq = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"

        while deq:
            row, col, steps = deq.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dy, col + dx
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                    if (nr == 0 or nr == m - 1) or (nc == 0 or nc == n - 1):
                        return steps + 1

                    maze[nr][nc] = "+"
                    deq.append((nr, nc, steps + 1))

        return -1