from collections import deque

def bfs(graph, start):
    visited = set()
    deq = deque([start])
    result = []
    while deq:
        x = deq.popleft()
        if x not in visited:
            visited.add(x)
            result.append(x)
            deq.extend(n for n in graph[x] if n not in visited)
    return result

# x = vertex
# n = neighbor