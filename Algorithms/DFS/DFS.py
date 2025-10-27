def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for n in graph[start]:
        if n not in visited:
            result.extend(dfs(graph, n, visited))
    return result

# n = neighbor