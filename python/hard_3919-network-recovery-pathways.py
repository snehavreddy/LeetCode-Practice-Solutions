import heapq
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        for u, v, cost in edges:
            adj[u].append((v, cost))
        
        # Helper function to check if a path exists with minimum edge cost >= min_val
        def check(min_val):
            # Distance array initialized to infinity
            dist = [float('inf')] * n
            dist[0] = 0
            
            # Using Dijkstra's to find the shortest path based on recovery cost
            # while ignoring edges with cost < min_val
            pq = [(0, 0)]  # (current_cost, u)
            
            while pq:
                d, u = heapq.heappop(pq)
                
                if d > dist[u]:
                    continue
                if u == n - 1:
                    return d <= k
                
                for v, cost in adj[u]:
                    if online[v] and cost >= min_val:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            heapq.heappush(pq, (dist[v], v))
            
            return dist[n - 1] <= k

        # Extract all unique edge costs to binary search over
        costs = sorted(list(set(edge[2] for edge in edges)))
        
        # Binary search for the maximum valid minimum-edge cost
        left = 0
        right = len(costs) - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if check(costs[mid]):
                ans = costs[mid]
                left = mid + 1
            else:
                right = mid - 1
                
        return ans