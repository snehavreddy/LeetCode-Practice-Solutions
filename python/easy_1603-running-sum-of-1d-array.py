class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSum = []
        sum = 0

        for num in nums:
            sum += num
            runningSum.append(sum)

        return runningSum 
        