class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # Instead of finding the minimum prefix and suffix, 
        # we find the longest contiguous subarray that sums to sum(nums) - x
        target = sum(nums) - x
        
        # If target is less than 0, it's impossible since all nums are positive
        if target < 0:
            return -1
        # If target is 0, we need to remove all elements
        if target == 0:
            return len(nums)
            
        max_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window if the sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # If we find a valid subarray, update the max length
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # If we didn't find any valid subarray, return -1
        return len(nums) - max_len if max_len != -1 else -1