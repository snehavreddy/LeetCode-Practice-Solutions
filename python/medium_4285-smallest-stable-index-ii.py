class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute the suffix minimums
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])
            
        # Keep track of the prefix maximum on the fly and find the smallest stable index
        pref_max = nums[0]
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            
            # Calculate instability score and check if it is <= k
            if pref_max - suff_min[i] <= k:
                return i
                
        return -1