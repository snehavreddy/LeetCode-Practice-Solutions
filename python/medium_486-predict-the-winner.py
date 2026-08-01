class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        
        def helper(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
            choose_left = nums[i] - helper(i + 1, j)
            choose_right = nums[j] - helper(i, j - 1)
            
            memo[(i, j)] = max(choose_left, choose_right)
            return memo[(i, j)]
        
        return helper(0, len(nums) - 1) >= 0