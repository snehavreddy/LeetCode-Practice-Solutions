from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # result[x] will store the total number of subarrays with product % k == x
        result = [0] * k
        
        # dp[r] stores the number of subarrays ending at the current index with product % k == r
        dp = [0] * k
        
        for num in nums:
            next_dp = [0] * k
            
            # 1. Start a new subarray with just the current element
            next_dp[num % k] += 1
            
            # 2. Extend existing subarrays that ended at the previous index
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    next_dp[new_r] += dp[r]
            
            # Add the current step's counts to the overall result
            for r in range(k):
                result[r] += next_dp[r]
                
            # Move to the next index
            dp = next_dp
            
        return result