class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # 'comp' will store the component ID for each node.
        # Nodes in the same component will have the same ID.
        comp = [0] * n
        
        # Iterate through the sorted array to assign component IDs.
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                # Still in the same component.
                comp[i] = comp[i-1]
            else:
                # Difference exceeds maxDiff; start a new component.
                comp[i] = comp[i-1] + 1
                
        # For each query, check if both nodes belong to the same component ID.
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])
            
        return ans