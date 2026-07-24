class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_vals = set(nums)
        current = {0}
        
        for _ in range(3):
            next_set = set()
            for x in current:
                for y in unique_vals:
                    next_set.add(x ^ y)
            current = next_set
            
        return len(current)