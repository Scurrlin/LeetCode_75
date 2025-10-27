# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left). Each
# asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids
# meet, the smaller one will explode. If both are the same size, both will
# explode. Two asteroids moving in the same direction will never meet.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if abs(a) > stack[-1]:
                    stack.pop()
                elif abs(a) < stack[-1]:
                    break 
                else:
                    stack.pop()
                    break 
            else:
                stack.append(a)
        return stack