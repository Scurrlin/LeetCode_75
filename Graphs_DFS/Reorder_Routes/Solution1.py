class Solution:
    def dfs(self, adj: List[List[Tuple[int, int]]], visited: List[bool], minChange: List[int], currCity: int) -> None:
        visited[currCity] = True
        for neighbourCity in adj[currCity]:
            if not visited[neighbourCity[0]]:
                if neighbourCity[1] == 1:
                    minChange[0] += 1
                self.dfs(adj, visited, minChange, neighbourCity[0])
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], -1))
        visited = [False] * n
        minChange = [0]
        self.dfs(adj, visited, minChange, 0)
        return minChange[0]