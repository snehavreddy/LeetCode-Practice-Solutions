class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Minimum is in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Minimum is at mid or to the left
                right = mid
            else:
                # nums[mid] == nums[right]
                # Cannot determine the side, safely shrink the search space from the right
                right -= 1
                
        return nums[left]