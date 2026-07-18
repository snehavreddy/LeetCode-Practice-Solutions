import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Find the minimum and maximum values in the array
        min_val = min(nums)
        max_val = max(nums)
        
        # Return the GCD of the min and max values
        return math.gcd(min_val, max_val)