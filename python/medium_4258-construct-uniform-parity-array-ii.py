class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Find the smallest element in the array
        min_val = min(nums1)
        
        # If the minimum is odd, we can make everything odd by subtracting it from the evens.
        if min_val % 2 != 0:
            return True
            
        # If the minimum is even, we can only succeed if ALL numbers in the array are even.
        return all(x % 2 == 0 for x in nums1)