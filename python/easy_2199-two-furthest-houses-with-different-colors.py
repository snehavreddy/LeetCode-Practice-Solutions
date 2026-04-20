class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        
        # Compare with first house
        for i in range(n):
            if colors[i] != colors[0]:
                ans = max(ans, i)
        
        # Compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                ans = max(ans, n - 1 - i)
        
        return ans    