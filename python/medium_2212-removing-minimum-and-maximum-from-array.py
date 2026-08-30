class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        
        # If the array has 2 or fewer elements, we have to remove all of them.
        if n <= 2:
            return n
        
        # Find the indices of the minimum and maximum elements in a single pass
        min_idx = 0
        max_idx = 0
        
        for k in range(1, n):
            if nums[k] < nums[min_idx]:
                min_idx = k
            elif nums[k] > nums[max_idx]:
                max_idx = k
                
        # Identify which index comes first and which comes second
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        # Scenario 1: Remove both from the front
        front_deletions = j + 1
        
        # Scenario 2: Remove both from the back
        back_deletions = n - i
        
        # Scenario 3: Remove from both ends
        both_ends_deletions = (i + 1) + (n - j)
        
        # Return the minimum deletions among the three scenarios
        return min(front_deletions, back_deletions, both_ends_deletions)