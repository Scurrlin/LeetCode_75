# There are some spherical balloons taped onto a flat wall that represents the
# XY-plane. The balloons are represented as a 2D integer array points where
# points[i] = [xstart, xend] denotes a balloon whose horizontal diameter
# stretches between xstart and xend. You do not know the exact y-coordinates of
# the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from
# different points along the x-axis. A balloon with xstart and xend is burst by
# an arrow shot at x if xstart <= x <= xend. There is no limit to the number of
# arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting
# any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot
# to burst all balloons.

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res, prev = len(points), points[0]

        for i in range(1, len(points)):
            curr = points[i]
            if curr[0] <= prev[1]:
                res -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr
        
        return res