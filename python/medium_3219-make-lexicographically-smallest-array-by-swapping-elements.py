class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        # Store tuples of (value, original_index) and sort them by value
        sorted_nums = sorted([(nums[i], i) for i in range(n)])
        
        result = [0] * n
        
        i = 0
        while i < n:
            j = i + 1
            # Group elements that are within the allowed limit difference
            while j < n and sorted_nums[j][0] - sorted_nums[j-1][0] <= limit:
                j += 1
            
            # Extract the original indices of the current component and sort them
            indices = [sorted_nums[k][1] for k in range(i, j)]
            indices.sort()
            
            # Place the sorted values into the earliest available sorted indices
            for k, idx in enumerate(indices):
                result[idx] = sorted_nums[i + k][0]
                
            i = j # Move to the next component
            
        return result