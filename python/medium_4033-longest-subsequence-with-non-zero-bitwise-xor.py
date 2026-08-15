class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # If all elements are 0, it's impossible to get a non-zero XOR
        if not any(nums):
            return 0
        
        # Calculate the total XOR of the entire array
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        # If the total XOR is already non-zero, we can use the whole array
        if total_xor != 0:
            return len(nums)
            
        # If total XOR is 0 (and not all elements are 0), 
        # removing one non-zero element makes the remaining XOR non-zero.
        return len(nums) - 1