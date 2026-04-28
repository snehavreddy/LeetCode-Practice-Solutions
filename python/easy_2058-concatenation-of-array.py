class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        newArry = [0] * (size * 2)
        for i in range(size):
            newArry[i] = nums[i]
            newArry[i + size] = nums[i]
        return newArry