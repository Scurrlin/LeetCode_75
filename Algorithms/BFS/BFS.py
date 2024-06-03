from collections import deque

def bfs(g, s):
    v = set()
    q = deque([s])
    result = []
    while q:
        x = q.popleft()
        if x not in v:
            v.add(x)
            result.append(x)
            q.extend(n for n in g[x] if n not in v)
    return result

# v = visited
# q = queue
# g = graph
# x = vertex
# s = start
# n = neighbor