from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        # Step 2: Find all suspicious methods starting from method k
        suspicious = set()
        stack = [k]
        suspicious.add(k)
        
        while stack:
            curr = stack.pop()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)
                    
        # Step 3: Check if any method outside the suspicious group invokes a method inside
        is_isolated = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                is_isolated = False
                break
                
        # Step 4: If not isolated, no methods can be removed. Return all methods.
        if not is_isolated:
            return list(range(n))
            
        # Otherwise, return all methods that are not suspicious
        return [i for i in range(n) if i not in suspicious]