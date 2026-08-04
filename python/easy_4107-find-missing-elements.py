class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)
        
        # Convert list to a set for O(1) lookups
        nums_set = set(nums)
        
        # Iterate through the range from min_val to max_val and find missing numbers
        missing = [x for x in range(min_val, max_val + 1) if x not in nums_set]
        
        return missing