class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for nums in nums_set:
            if nums - 1 not in nums_set:
                current = nums + 1
                length = 1
                while current in nums_set:
                    length+=1
                    current+=1
                longest = max(longest, length)
        return longest