from typing import List
from itertools import accumulate

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Calculate the prefix sums of the stones array
        prefix_sums = list(accumulate(stones))
        
        # Base case: the score if the current player takes all remaining stones
        dp = prefix_sums[-1]
        
        # Work backwards from the second-to-last choice down to index 1
        # Index 1 corresponds to choosing exactly 2 stones (the minimum allowed)
        for i in range(len(stones) - 2, 0, -1):
            dp = max(dp, prefix_sums[i] - dp)
            
        return dp