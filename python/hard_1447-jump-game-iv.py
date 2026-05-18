from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Step 1: Map each value to all its indices
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        # Step 2: Initialize BFS queue and visited set
        # Stores tuples of (current_index, current_steps)
        queue = deque([(0, 0)])
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            
            # If we've reached the last index, return the steps taken
            if idx == n - 1:
                return steps
                
            # Step 3: Explore neighbors
            neighbors = []
            
            # Jump to i + 1
            if idx + 1 < n:
                neighbors.append(idx + 1)
            # Jump to i - 1
            if idx - 1 >= 0:
                neighbors.append(idx - 1)
                
            # Jump to other indices with the same value
            if arr[idx] in graph:
                neighbors.extend(graph[arr[idx]])
                # CRITICAL OPTIMIZATION: Clear the list for this value so 
                # we don't redundant-loop over it from another index.
                del graph[arr[idx]]
                
            # Process all valid neighbors
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
                    
        return -1