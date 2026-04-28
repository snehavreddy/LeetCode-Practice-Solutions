class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newArr = [0] * len(nums)
        j = 0
        for i in range(n):
            newArr[j] = nums[i]
            newArr[j + 1] = nums[i + n]
            j = j + 2
            
        return newArr