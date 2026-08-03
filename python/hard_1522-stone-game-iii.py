from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp array of size 4 to store the max score difference for the next 3 states
        dp = [0] * 4
        
        for i in range(n - 1, -1, -1):
            j = i % 4
            # Take 1 stone
            res = stoneValue[i] - dp[(i + 1) % 4]
            
            # Take 2 stones
            if i + 1 < n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] - dp[(i + 2) % 4])
            
            # Take 3 stones
            if i + 2 < n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[(i + 3) % 4])
            
            dp[j] = res
            
        final_diff = dp[0]
        if final_diff > 0:
            return "Alice"
        elif final_diff < 0:
            return "Bob"
        else:
            return "Tie"