class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
      
        graph = [[] for _ in range(n)]

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        tin = [-1] * n
        low = [-1] * n
        timer = 0
        bridges = []

        def dfs(node, parent):
            nonlocal timer

            tin[node] = low[node] = timer
            timer += 1

            for nei in graph[node]:

                if nei == parent:
                    continue

                if tin[nei] != -1:  # back edge
                    low[node] = min(low[node], tin[nei])

                else:  # tree edge
                    dfs(nei, node)

                    low[node] = min(low[node], low[nei])

                    if low[nei] > tin[node]:
                        bridges.append([node, nei])

        dfs(0, -1)

        return bridges
        
        