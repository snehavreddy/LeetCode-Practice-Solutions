class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numCount = 0
        for num in nums:
            digCount = 0
            while num > 0:
                digCount +=1
                num //= 10
            if digCount & 1 == 0:
                numCount+=1
        return numCount    