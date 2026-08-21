import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        
        # Precompute the LCM for all non-empty subsets of coins
        # There are 2^n - 1 non-empty subsets
        for mask in range(1, 1 << n):
            current_lcm = 1
            set_bits = 0
            
            for i in range(n):
                if mask & (1 << i):
                    current_lcm = math.lcm(current_lcm, coins[i])
                    set_bits += 1
            
            # According to the Principle of Inclusion-Exclusion:
            # Odd number of elements -> Add to the count (+1)
            # Even number of elements -> Subtract from the count (-1)
            sign = 1 if set_bits % 2 == 1 else -1
            subsets.append((current_lcm, sign))
            
        def count_amounts_up_to(x: int) -> int:
            """Counts how many valid amounts can be formed that are <= x."""
            count = 0
            for lcm_val, sign in subsets:
                count += sign * (x // lcm_val)
            return count

        # Binary Search Range
        # Minimum possible valid amount is 1
        # Maximum possible valid amount is if we just use the smallest coin k times
        left = 1
        right = min(coins) * k
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            # If the number of combinations is at least k, 
            # this mid could be the answer, but we look for a smaller one.
            if count_amounts_up_to(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans