class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # minimum is on right side
            if nums[mid] > nums[right]:
                left = mid + 1

            # minimum is at mid or left side
            else:
                right = mid

        return nums[left]