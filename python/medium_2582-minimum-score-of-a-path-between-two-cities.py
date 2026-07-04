from collections import deque, defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        
        # BFS to find the minimum edge in the connected component
        min_score = float('inf')
        visited = set()
        queue = deque([1])
        visited.add(1)
        
        while queue:
            u = queue.popleft()
            for v, dist in graph[u]:
                # The score of the path is the minimum edge in the path
                min_score = min(min_score, dist)
                
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
                    
        return min_score