class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Find the sum of the longest sequential prefix starting at index 0
        prefix_sum = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1
        
        # Step 2: Look up the smallest missing integer >= prefix_sum
        num_set = set(nums)
        ans = prefix_sum
        while ans in num_set:
            ans += 1
            
        return ans