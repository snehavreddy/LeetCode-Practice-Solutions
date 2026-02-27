class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        for i in range(n - 2, -1, -1): # right prod
            result[i] = result[i + 1] * nums[i + 1]
        leftProd = 1
        for i in range(n):
            result[i] *= leftProd
            leftProd *= nums[i]
        return result