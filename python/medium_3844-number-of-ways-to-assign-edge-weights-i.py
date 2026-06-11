class Solution:
    MOD = 10**9 + 7

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            depth = 0

            for nei in adj[node]:
                if nei != parent:
                    depth = max(depth, 1 + dfs(nei, node))

            return depth

        max_depth = dfs(1, 0)

        return pow(2, max_depth - 1, self.MOD)