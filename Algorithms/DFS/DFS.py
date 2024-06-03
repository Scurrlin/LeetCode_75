def dfs(g, s, v = None):
    if v is None:
        v = set()
    v.add(s)
    result = [s]
    for n in g[s]:
        if n not in v:
            result.extend(dfs(g, n, v))
    return result

# g = graph
# s = start
# v = visited
# n = neighbor