class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = nums[-1]

        return nums == list(range(1, n + 1)) + [n]