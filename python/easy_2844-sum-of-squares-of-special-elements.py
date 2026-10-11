class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        # Using a generator expression to sum the squares of special elements
        return sum(nums[i] ** 2 for i in range(n) if n % (i + 1) == 0)