# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the ith day to get a warmer temperature. If there is no future day
# for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        res = [0] * len(T)
        stack = []

        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res