class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(num):
            total = 0
            
            while num > 0:
                total += num % 10
                num //= 10
            
            return total
        
        mini = float('inf')
        
        for num in nums:
            mini = min(mini, digit_sum(num))
        
        return mini