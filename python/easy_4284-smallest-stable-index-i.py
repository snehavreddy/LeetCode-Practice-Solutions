class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute the suffix minimums
        # suf_min[i] will store the minimum value in nums[i..n-1]
        suf_min = [0] * n
        suf_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])
            
        pref_max = nums[0]
        
        # Iterate to find the first index satisfying the condition
        for i in range(n):
            # Update the running maximum for nums[0..i]
            pref_max = max(pref_max, nums[i])
            
            # Calculate instability score and check against k
            if pref_max - suf_min[i] <= k:
                return i
                
        return -1