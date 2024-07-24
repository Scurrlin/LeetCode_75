# You are given a 0-indexed integer array costs where costs[i] is the cost of
# hiring the ith worker.

# You are also given two integers k and candidates. We want to hire exactly k
# workers according to the following rules:

# You will run k sessions and hire exactly one worker in each session. In each
# hiring session, choose the worker with the lowest cost from either the first
# candidates workers or the last candidates workers. Break the tie by the
# smallest index. For example, if costs = [3,2,7,7,1,2] and candidates = 2, then
# in the first hiring session, we will choose the 4th worker because they have
# the lowest cost [3,2,7,7,1,2]. In the second hiring session, we will choose
# 1st worker because they have the same lowest cost as 4th worker but they have
# the smallest index [3,2,7,7,2]. Please note that the indexing may be changed
# in the process. If there are fewer than candidates workers remaining, choose
# the worker with the lowest cost among them. Break the tie by the smallest
# index. A worker can only be chosen once. Return the total cost to hire exactly
# k workers.

class Solution:
    def totalCost(self, costs, k, candidates):
        i = 0
        j = len(costs) - 1
        pq1 = []
        pq2 = []

        ans = 0
        while k > 0:
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i])
                i += 1
            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2, costs[j])
                j -= 1

            t1 = pq1[0] if pq1 else float('inf')
            t2 = pq2[0] if pq2 else float('inf')

            if t1 <= t2:
                ans += t1
                heapq.heappop(pq1)
            else:
                ans += t2
                heapq.heappop(pq2)

            k -= 1
        return ans