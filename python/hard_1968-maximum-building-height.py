class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # 1. Add base constraints
        # Ensure [1, 0] is present and sort restrictions
        restrictions.append([1, 0])
        restrictions.sort()
        
        # Ensure the last building is included if not already there
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
            
        m = len(restrictions)
        
        # 2. Forward pass: Propagate constraints left to right
        for i in range(1, m):
            restrictions[i][1] = min(
                restrictions[i][1], 
                restrictions[i-1][1] + (restrictions[i][0] - restrictions[i-1][0])
            )
            
        # 3. Backward pass: Propagate constraints right to left
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1], 
                restrictions[i+1][1] + (restrictions[i+1][0] - restrictions[i][0])
            )
            
        # 4. Calculate maximum height between segments
        max_h = 0
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            
            # Formula for peak height between two restricted points
            # peak = (h1 + h2 + (id2 - id1)) // 2
            current_max = (h1 + h2 + (id2 - id1)) // 2
            max_h = max(max_h, current_max)
            
        return max_h