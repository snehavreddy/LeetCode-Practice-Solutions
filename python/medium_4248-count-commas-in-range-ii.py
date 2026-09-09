class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        base = 1000
        
        while n >= base:
            total_commas += (n - base + 1)
            base *= 1000
            
        return total_commas