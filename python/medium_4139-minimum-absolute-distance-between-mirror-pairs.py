class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            return int(str(x)[::-1])
        
        last_seen = {}
        ans = float('inf')
        
        for i, num in enumerate(nums):
            
            # check if current number matches any previous reverse
            if num in last_seen:
                ans = min(ans, i - last_seen[num])
            
            # store reverse for future matches
            rev = reverse(num)
            last_seen[rev] = i
        
        return ans if ans != float('inf') else -1