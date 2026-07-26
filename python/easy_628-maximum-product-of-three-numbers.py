class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # Option 1: Product of the three largest elements
        # Option 2: Product of the two smallest (negative) elements and the largest element
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])