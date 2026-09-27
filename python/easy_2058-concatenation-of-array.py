class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # size = len(nums)
        # ans = [None] * 2 * size

        # for idx, num in enumerate(nums):
        #     ans[idx] = ans[idx + size] = num

        # return list(ans)
        # return nums * 2
        return nums + nums