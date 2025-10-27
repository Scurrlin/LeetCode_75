# You are given an array of variable pairs equations and an array of real
# numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
# equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
# single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the
# jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined,
# return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries
# will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined,
# so the answer cannot be determined for them.

import collections 

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph, res = collections.defaultdict(list), []
        for equation, value in zip(equations, values):
            dividend, divisor = equation
            graph[dividend].append((divisor, value))
            graph[divisor].append((dividend, 1 / value))
        
        def dfs(dividend, divisor, visited, total):
            if dividend == divisor:
                return total
            if dividend not in visited:
                visited.add(dividend)

                for next_dividend, value in graph[dividend]:
                    if next_dividend not in visited:
                        ret = dfs(next_dividend, divisor, visited, total * value)
                        if ret != -1:
                            return ret
                        
            return -1

        for q in queries:
            dividend, divisor = q[0], q[1]
            if dividend not in graph or divisor not in graph:
                res.append(-1)
            else:
                ret = dfs(dividend, divisor, set(), 1)
                res.append(ret)        
        return res