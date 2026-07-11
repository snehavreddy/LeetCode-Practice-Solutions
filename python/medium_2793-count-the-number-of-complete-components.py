from collections import deque, defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                # Start BFS/DFS to find all nodes in this component
                component_nodes = []
                queue = deque([i])
                visited[i] = True
                
                while queue:
                    u = queue.popleft()
                    component_nodes.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append(v)
                
                # Check if component is complete
                # A component is complete if every node has degree == v - 1
                v_count = len(component_nodes)
                edge_count = 0
                for node in component_nodes:
                    edge_count += len(adj[node])
                
                # edge_count here is 2 * number of actual edges 
                # because each edge is counted twice in adjacency list
                if edge_count == v_count * (v_count - 1):
                    complete_components += 1
                    
        return complete_components