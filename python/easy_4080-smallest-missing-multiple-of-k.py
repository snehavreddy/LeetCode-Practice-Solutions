class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Convert the list to a set for O(1) lookups
        num_set = set(nums)
        
        # Start with the first positive multiple of k
        multiple = k
        
        # Keep incrementing by k until we find a multiple not in the set
        while multiple in num_set:
            multiple += k
            
        return multiple