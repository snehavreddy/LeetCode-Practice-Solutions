import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        
        # 1. Construct prefixGcd array
        current_max = 0
        for x in nums:
            if x > current_max:
                current_max = x
            # gcd(nums[i], mx_i)
            prefixGcd.append(math.gcd(x, current_max))
        
        # 2. Sort in non-decreasing order
        prefixGcd.sort()
        
        # 3. Form pairs (smallest + largest) and sum their GCDs
        total_gcd_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_gcd_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_gcd_sum